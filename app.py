from flask import Flask, render_template, send_file, request, redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

shared_folder = '/Users/naga/Downloads/shared'

def get_folder_contents(folder_path):
    contents = []
    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)
        if os.path.isfile(path):
            contents.append({'name': name, 'type': 'file'})
        elif os.path.isdir(path):
            contents.append({'name': name, 'type': 'folder'})
    return contents

@app.route('/')
def index():
    folder = request.args.get('folder')
    folder_path = os.path.join(shared_folder, folder) if folder else shared_folder
    if os.path.isdir(folder_path):
        folder_contents = get_folder_contents(folder_path)
        return render_template('index.html', folder_contents=folder_contents, current_folder=(folder or shared_folder))
    else:
        return "Invalid folder path"

@app.route('/files')
def download_file():
    folder = request.args.get('folder')
    filename = request.args.get('filename')
    folder_path = os.path.join(shared_folder, folder)
    file_path = os.path.join(folder_path, filename)
    return send_file(file_path, as_attachment=True)

@app.route('/navigate')
def navigate():
    folder = request.args.get('folder')
    return redirect(url_for('index', folder=folder))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
