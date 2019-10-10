import os 
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId



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
def files_new():
    """Create a new file."""
    return render_template('new_files.html', files={}, title='New File', stl="")


#SUBMIT
@app.route('/files/new', methods=['POST'])
def files_():
    """Submit a new playlist."""
    stl = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    stls = files.insert_one(stl).inserted_id
    return redirect(url_for('files_show', file_id=stls))
    
#ID
@app.route('/files/<file_id>')
def files_show(file_id):
    """Show a single file."""
    file_id = files.find_one({'_id': ObjectId(file_id)})
    return render_template('files_show.html', stl=file_id)

@app.route('/files/<file_id>', methods=['POST'])
def files_update(file_id):
    """Submit an edited playlist."""
    updated_stl = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    files.update_one(
        {'_id': ObjectId(file_id)},
        {'$set': updated_stl})
    return redirect(url_for('files_show', file_id=file_id))

@app.route('/files/<file_id>/edit')
def playlists_edit(file_id):
    """Show the edit form for a file."""
    stls = files.find_one({'_id': ObjectId(file_id)})
    return render_template('files_edit.html', stl=stls, title='Edit Files')

@app.route('/files/<file_id>/delete', methods=['POST'])
def playlists_delete(file_id):
    """Delete one file."""
    files.delete_one({'_id': ObjectId(file_id)})
    return redirect(url_for('stl_index'))


if __name__ == '__main__':
    app.run(debug=True)