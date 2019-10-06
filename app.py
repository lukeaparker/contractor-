from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Return homepage."""
    return render_template('home.html', msg=files)

files = [
    { 'title': 'Cat', 'description': '3D Model of Cat' },
        { 'title': 'Cat', 'description': '3D Model of Cat' },
]

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)