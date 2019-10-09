import os 
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Files')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
files = db.files 

app = Flask(__name__)

#MOCK JSON DATA
# files = [
#     { 'title': 'Cat', 'description': 'Cat .gcode file sliced for ender 3.' },
#     { 'title': 'Building', 'description': 'Building .gcode file sliced for ender 3.' }
# ]

#HOMEPAGE
@app.route('/')
def stl_index():
    """Show all playlists."""
    return render_template('files_index.html', files=files.find())

#NEW
@app.route('/files/new')
def stl_new():
    """Create a new file."""
    return render_template('new_files.html', files={}, title='New File')

#SUBMIT
@app.route('/files', methods=['POST'])
def show_index():
    """Submit a new playlist."""
    stl = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    stls = files.insert_one(stl).inserted_id
    return redirect(url_for('stl_index', stls=stls))


if __name__ == '__main__':
    app.run(debug=True)