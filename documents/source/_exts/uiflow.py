# -*- coding: utf-8 -*-
import codecs
import errno
import hashlib
import os
import re
import shlex
import subprocess
from contextlib import contextmanager

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from sphinx.errors import SphinxError
from sphinx.util.nodes import set_source_info
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import (
    ensuredir,
    ENOENT,
)

class uiflow(nodes.General, nodes.Element):
    pass

def depart_uiflow_node(self, node):
    self.depart_admonition(node)

class UiflowDirective(SphinxDirective):
    has_content = True
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env
        node = uiflow(self.block_text, **self.options)
        filename = self.arguments[0]
        relname, absname = env.relfn2path(filename)
        env.note_dependency(relname)
        node['incdir'] = os.path.dirname(relname)
        node['filename'] = absname
        return [node]

def purge_uiflows(app, env, docname):
    pass

def generate_name(self, node, fileformat):
    h = hashlib.sha1()
    # may include different file relative to doc
    h.update(node['incdir'].encode('utf-8'))
    h.update(b'\0')
    h.update(node['filename'].encode('utf-8'))
    key = h.hexdigest()
    fname = 'uiflow-%s.%s' % (key, fileformat)
    imgpath = getattr(self.builder, 'imgpath', None)
    if imgpath:
        return ('/'.join((self.builder.imgpath, fname)),
                os.path.join(self.builder.outdir, '_images', fname))
    else:
        return fname, os.path.join(self.builder.outdir, fname)

def visit_uiflow_node(self, node):
    refname, outfname = generate_name(self, node, 'png')
    # if os.path.exists(outfname):
    #     return refname, outfname
    ensuredir(os.path.dirname(outfname))

    # uiflow -i myapp.txt -o myapp.png -f png  
    p = subprocess.run(
        [
            'bash',
            self.builder.config.uiflow_exepath,
            node['filename'],
            outfname
        ])
    # if p.returncode != 0:
    #     pass

    self.body.append(self.starttag(node, 'p', CLASS='uiflow'))
    self.body.append('<img style="max-width: 100%%;" src="%s" alt="flow"/>\n' % (self.encode(refname)))
    self.body.append('</p>\n')
    raise nodes.SkipNode

def setup(app):
    app.add_node(uiflow,
                 html=(visit_uiflow_node, depart_uiflow_node))

    app.add_config_value('uiflow_exepath',
        os.path.abspath('../extensions/call-uiflow.sh'),
        'html')
    app.add_directive('uiflow', UiflowDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True
    }
