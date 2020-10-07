from flask import Flask, render_template, request, session
from flask_session import Session
from ArtistAnalizer import ArtistAnalizer

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False 
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def index():
    session['artist_name'] = ""  
    session['songs'] = []
    return render_template('index.html')

@app.route('/discography', methods = ['POST'])
def discography():
    name = request.form.get('name')
    name = name.capitalize()
    session['artist_name'] = name
    artist = ArtistAnalizer(name)
    id = artist.artistId()
    if id == False:
        return render_template('notfound.html',name = name)
    records = artist.artistRecords(id)
    return render_template('discography.html', name = name, records = records)


@app.route('/<string:release>', methods= ['GET','POST'])
def release(release): 
    artist = ArtistAnalizer(session['artist_name'])
    songs = artist.releaseSongs(session['artist_name'],release)
    if songs != False:
        session['songs'] = songs
    if songs == False:
        return render_template('notfound.html')
    return render_template('songs.html', songs = songs, release = release)


@app.route('/average')
def average():
    print(session['artist_name'])
    print(session['songs'])
    artist = ArtistAnalizer(session['artist_name'])
    print(session['artist_name'])
    mean = artist.analizeLyrics(session['artist_name'],session['songs'])
    session['songs'] = []
    return render_template('average.html', mean = mean)


if __name__ == "__main__":
    app.run(debug = True)