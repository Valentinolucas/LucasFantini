import musicbrainzngs
import requests
import json


class ArtistAnalizer():


    def __init__(self,name):
        musicbrainzngs.set_useragent('MyFirstApp','V1.0')
        self.name = name.capitalize()
    

    def artistId(self):
        '''
        Get the artist ID from musicbrainzngs API
            Args:
                artist = "Artist Name" (String)
            Return:
                Id = Id of the artist  (string)
        '''
        result = musicbrainzngs.search_artists(artist=self.name, type="group", limit = 1)
        for artist in result['artist-list']:
            if artist['name'].capitalize() in self.name:
                id = artist['id']
                name = artist['name']
                return id
            else:
                return False
        
        

    def artistRecords(self, id):
        '''
        Get the artist releases from musicbrainzngs API
            Args:
                id = 'Artist Id in API' (string)
            Returns:
                records = list of records (list)
        '''
        self.id = id
        releases = []
        try:
            result = musicbrainzngs.get_artist_by_id(
                        self.id,
                        includes=["release-groups"], release_type=["album", "ep"])
        except:
            return False 
        else:
            for release_group in result["artist"]["release-group-list"]:
                if release_group['type']!='Live':
                    releases.append(release_group['title'])
            return releases
        

    def releaseSongs(self,artist,release_name):
        '''
        Get the tracklist from a specific release
            Args:
                artist = 'artist name' (string)
                release_name = 'release_name' (string)
        '''
        self.artist = artist
        self.release_name = release_name
        try:
            result = musicbrainzngs.search_releases(query=self.release_name, 
                                                    limit=None, 
                                                    offset=None, 
                                                    strict=True, artist=self.artist )
            
            releaseId = result['release-list'][0]['id']

            result = musicbrainzngs.get_release_by_id(releaseId, 
                                                        includes=['recordings'], 
                                                        release_status=[], 
                                                        release_type=[])
            
            tracklist = result['release']['medium-list'][0]['track-list']
            output = []
            for track in tracklist:
                output.append(track['recording']['title'])
            return output
        except:
            return False
        

    
    def analizeLyrics(self,artist, songs):
        '''
        Get the lyrics from a list of songs and calculates the average amount of words

        Args:
            lyric = list of words (list)
        Returs:
            mean = average words (float)
        '''
        self.artist = artist
        self.songs = songs
        resultado = []
        for song in songs:
            try:
                API_KEY = 'yVpCjLgQlZLKpvuzTPLz2vKLyq8Z6elji561CphxvEmMo4X4CL9jGn2ZpMdjqInZ' #this should be saved in an enviroment variable if the app is published
                url = 'https://orion.apiseeds.com/api/music/lyric/{artist}/{song}?apikey={key}'.format(artist = self.artist, song = song, key = API_KEY)
                res = requests.get(url)
                res = json.loads(res.content)
                count = len(res['result']['track']['text'].split())
                resultado.append(count)
            except:
                pass
        if len(resultado)>0: 
            mean = sum(resultado)/len(resultado)
            return mean
     
            
            
    
