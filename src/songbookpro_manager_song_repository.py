from base_song_repository import BaseSongRepository
import requests
from song import Song

class SongbookProManagerSongRepository(BaseSongRepository):

    def __init__(self, ip_address: str, port: str, session: requests.Session):
        self.session = session
        self.base_url = f"http://{ip_address}:{port}"
        self.set_headers()
        self._fetch_all_songs()

    def find_by_name(self, name: str) -> Song:
        for song in self.all_songs:
            if self._matches(name, song):
                return song
        return None

    def _fetch_all_songs(self):
        response = self.session.get(self.base_url + "/api/editor/songs")
        songs_json = response.json()
        self.all_songs = [Song(song['Id'], song['name'], song['author'], song['key'], song['subTitle'], song['KeyShift']) for song in songs_json]

    def _matches(self, name: str, song: Song):
        if name in song.name:
            return True
        if name == song.subtitle:
            return True
        if name == f"{song.name} ({song.author})":
            return True
        return False
    
    def set_headers(self):
        print('Waiting for approval from application...')
        self.session.get(self.base_url + "/api/editor/songs")
        cookies = self.session.cookies.get_dict()
        self.cookie = cookies['jagses']
        self.headers = {"Cookie": f"jagses={self.cookie}"}