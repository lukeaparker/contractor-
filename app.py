from flask import Flask, render_template

app = Flask(__name__)


playlists = [
    { 'title': 'Cat', 'description': 'Cat .gcode file sliced for ender 3.' },
    { 'title': 'Building', 'description': 'Building .gcode file sliced for ender 3.' }
]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('files_index.html', playlists=playlists)


if __name__ == '__main__':
    app.run(debug=True)