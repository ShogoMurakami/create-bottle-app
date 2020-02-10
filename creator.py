# -*- coding: utf-8 -*-

import os

project_name = input("Project Name: ")

new_static_path = project_name + '/static'
new_views_path = project_name + '/views'

# static,viewsフォルダの作成
os.makedirs(new_static_path)
os.makedirs(new_views_path)

framework = int(input("""Choose your favorite UI framework.
1.Bootstrap4, 2.Semantic UI, 3.None
Enter number: """))

# index.htmlの作成

index_str = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="../static/main.css">

    <title>""" + project_name + """</title>

  </head>
  <body>

    <h1 class="first-message">{{message}}</h1>

  </body>
</html>
"""

new_index = open(new_views_path + '/index.html', 'w')
new_index.write(index_str)
new_index.close()

# main.cssの作成

css_str = """.first-message {
    padding-top:100px;
}
"""

new_css = open(new_static_path + '/main.css', 'w')
new_css.write(css_str)
new_css.close()

# app.pyの作成

py_str = """# -*- coding: utf-8 -*-

from bottle import Bottle, template, static_file, url
import os

app = Bottle()

@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@app.route('/')
def index():
    message = "Hello, Bottle!"
    return template('index', message=message)

@app.error(404)
def error404(error):
    return "Error 404. Try again later."

@app.error(500)
def error500(error):
    return "Error 500. Try again later."

# localでtestする
app.run(host='localhost', port=8080, debug=True)

# Herokuにデプロイする場合
# app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

"""

new_python_file = open(project_name + '/app.py', 'w')
new_python_file.write(py_str)
new_python_file.close()

print("DONE")
