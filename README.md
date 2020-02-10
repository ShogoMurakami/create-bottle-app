# create-bottle-app

PythonのWEBフレームワーク"[Bottle](https://bottlepy.org/docs/dev/)"を利用する際に、最低限必要なファイルやフォルダを自動的に生成します。

Bottleは以下のコマンドでインストールすることができます。

```
$ pip install bottle
```

# creator.py

creator.pyを以下のコマンドで実行します。

```
$ python creator.py
```

プロジェクト名を聞かれるので、入力します。

次に、利用するUIフレームワークを聞かれるので、数字で入力します。

その後、自動的にフォルダとファイルが生成されます。

# 作成後

フォルダとファイルが作成されたら、プロジェクトフォルダに移動し、app.pyを実行してみて下さい。

```
$ python app.py
```

実行後、localhost:8080 を開くと、Hello, Bottle!が表示されるはずです。

あとは、あなたのBottleプロジェクトを充実させていきましょう！

