from flask import Flask, render_template,abort
import os
import json

app = Flask(__name__)

def get_all_files():
    files = {}
    for filename in os.listdir('/home/shiyanlou/files'):
        with open('/home/shiyanlou/files'+'/' + filename) as f:
            files[filename[:-5]]= json.load(f)
        return files

files = get_all_files()

@app.route('/')
def index():
    titles = [item['title'] for item in files.values()]
    return render_template('index.html',titles=titles)

@app.route('/files/<filename>')
def file(filename):
    file_item = files.get(filename)
    if file_item is None:
        abort(404)
    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
