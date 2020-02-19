FROM node:latest
USER root
RUN apt-get update -qq

# ja: pythonに必要なパッケージを取得
# en: Install required packages by python.
RUN apt-get install -y default-jre graphviz build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget locales


# ja: 日本の設定
# en: Setting locale for Japanese.
#     Change "TimeZone, fonts and Language" If you use other than Japanese.
#     e.g.) Chinese, Arabic
#           Maybe English is not.
RUN apt-get install -y fonts-horai-umefont
ENV TZ Asia/Tokyo
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LANGUAGE ja

RUN npm install -g uiflow

WORKDIR /tmp/python

# ja: python3とpipインストール
# en: Install python3 and pip.
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz && \
    tar xvf Python-3.7.0.tar.xz && \
    cd Python-3.7.0 && \
    ./configure && \
    make altinstall

RUN apt-get install -y python3-pip
# python3-sphinx

# ja: Sphinxのインストール
# en: Install Sphinx
RUN pip3 install docutils sphinx sphinxcontrib-plantuml sphinxcontrib-websupport
