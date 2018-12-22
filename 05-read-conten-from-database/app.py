#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'  #浏览器访问主页面会显示一个 'Hello Worle!'

if __name__ == '__main__':
    app.run()
