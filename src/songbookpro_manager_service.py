import requests
from song import Song
from set_item import SetItem

class SongbookProManagerService:

    def __init__(self, ip_address):
        self.url = f"http://{ip_address}:8080"
        self.session = requests.Session()
        self._set_headers()

    def _set_headers(self):
        print('Waiting for approval from application...')
        self.session.get(self.url + "/api/editor/songs")
        cookies = self.session.cookies.get_dict()
        self.cookie = cookies['jagses']
        if not self.cookie:
            print("Failed to retrieve session cookie.")
            exit(1)
        self.headers = {"Cookie": f"jagses={self.cookie}"}

    def _find_all_songs(self):
        """
        Fetch all songs from SongbookPro.
        """
        response = self.session.get(self.url + "/api/editor/songs")
        songs_json = response.json()
        songs = [Song(song['Id'], song['name'], song['key'], song['subTitle'], song['KeyShift']) for song in songs_json]
        return songs

    def _add_song(self, set_id: int, set_item: SetItem):
        response = self.session.post(self.url + f"/api/arrange/setItem", headers=self.headers, json={"order": set_item.order, "setId": set_id, "songId": set_item.song.id, "type": 1})
        set_item_id = response.json()["setItem"]["Id"]
        if set_item.set_key > 0:
            response = self.session.put(self.url + "/api/arrange/setItem", headers=self.headers, json=[{"id": set_item_id, "data": {"keyOfset": set_item.key_offset()}}])
    
    def create_set(self, set_name: str, matched_songs: list):
        response = self.session.post(self.url + "/api/arrange/sets", headers=self.headers)
        set_id = response.json()["Id"]
        self.session.put(self.url + f"/api/arrange/sets/{set_id}", json={"name": set_name})
        for matched_song in matched_songs:
            self._add_song(set_id, matched_song)
        print(f"Set '{set_name}' created successfully!")