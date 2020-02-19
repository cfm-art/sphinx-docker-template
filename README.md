Sphinx Docker Compose Template
==

名前の通り、ドキュメント作成ツールの `Sphinx` の `Docker Compose` 用のテンプレートです。  
たぶん動いています。

## ライセンス
MIT

## 使い方

1. `Clone or Download` からZIPをダウンロード
1. ZIPを解凍
1. (必要があれば) Dockerfile を変更
1. (必要があれば) docker-compose.yml を変更
1. (必要があれば) plantuml をインストール
1. documents/source/conf.py を変更
1. rstを記述する

### `Clone or Download` からZIPをダウンロード
githubの　`Clone or Download` ボタンを押し、 `Download ZIP` を押す。

### ZIPを解凍
してください。

### (必要があれば) Dockerfile を変更
必要があれば変更してくだいさい。

npmが手軽に欲しかったため、nodeイメージをベースにしています。  
※ nodeイメージはdebianのようです。  
※ `python3-sphinx` ではうまくビルドができなかったのでpip3のsphinxパッケージを使っています。

### (必要があれば) docker-compose.yml を変更
必要があれば変更してくだいさい。

### (必要があれば) plantuml をインストール
plantumlをドキュメント内で利用したい場合は公式から取得してください。  
※ `plantuml.jar` の保存された場所は把握しておいてください。

### documents/source/conf.py を変更
ドキュメントの設定を行う `conf.py` を編集します。  
細かい設定は `Sphinx` の[公式](https://www.sphinx-doc.org/ja/master/usage/quickstart.html)を参照してください。

- project = 'Sphinx-docker-template'
    - ドキュメントのタイトルへ変更します。
- copyright = 'art'
    - コピーライトへ変更します。
- author = 'art'
    - 記述者へ変更します。
- version = '0.0.0'
    - ドキュメントバージョンへ随時変更します。
- release = '0.0.0'
    - ドキュメントバージョンへ随時変更します。
- `#` 'sphinxcontrib.plantuml',
    - plantumlを利用する場合は、先頭の `#` を取り除きます。
- plantuml_path = os.path.abspath('../extensions/plantuml.jar')
    - plantumlを利用する場合は、 `plantuml.jar`  のパスへ変更します。  
    documents/extensionsフォルダへ配置した場合は変更は不要です。

### rstを記述する
好きなようにrstを記述してください。

## 番外: uiflowについて
uiflow用の拡張を適当に作って含めています。

```rst
.. uiflow:: ファイル名
```

と記述することで使えます。

ファイルを用意しない以下のような形には対応させていません。

```rst
.. uiflow::

    これはうごきません。
```

# English

Machine translation.
Is this English correct?

## Usage

1. Download ZIP from `Clone or Download`
1. Uncompress the ZIP
1. (if necessary) Change Dockerfile
1. (if necessary) Change docker-compose.yml
1. (if necessary) Install plantuml
1. Change documents/source/conf.py
1. Just as you like write rst

### Download ZIP from `Clone or Download`
Press `Clone or Download` in this github page and Press `Download ZIP`.

### Uncompress the ZIP
Do it.

### (if necessary) Change Dockerfile
If necessary, you change it.

This Image is from the node image.
Cuz I need npm easily.

### (if necessary) Change docker-compose.yml
If necessary, you change it.

### (if necessary) Install plantuml
If you will use plantuml in sphinx, you get plantuml from offical site.
※ Do not forget installed-path.

### Change documents/source/conf.py
Change `conf.py`.
If you want to know details of setting, you look [sphinx offical site](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

- project = 'Sphinx-docker-template'
    - Modify document title
- copyright = 'art'
- author = 'art'
- version = '0.0.0'
    - Keep document version it updated.
- release = '0.0.0'
    - Keep document version it updated.
- `#` 'sphinxcontrib.plantuml',
    - if use plantuml, remove `#`.
- plantuml_path = os.path.abspath('../extensions/plantuml.jar')
    - if use plantuml, change to installed-path of `plantuml.jar`  
    if installed to `documents/extensions`, you do not it.

### Just as you like write rst
Just as you like.

