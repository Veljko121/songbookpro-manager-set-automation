from base_set_repository import BaseSetRepository
from set import Set
from set_item import SetItem
from typing import List
import requests

class SongbookProManagerSetRepository(BaseSetRepository):

    def __init__(self, ip_address: str, port: str, session: requests.Session):
        self.session = session
        self.base_url = f"http://{ip_address}:{port}"
        self.set_headers()

    def save(self, set: Set):
        response = self.session.post(self.base_url + "/api/arrange/sets", headers=self.headers)
        set_id = response.json()["Id"]
        self.session.put(self.base_url + f"/api/arrange/sets/{set_id}", json={"name": set.name})
        for i, set_item in enumerate(set.items):
            response = self.session.post(self.base_url + f"/api/arrange/setItem", headers=self.headers, json={"order": i, "setId": set_id, "songId": set_item.song.id, "type": 1})
            set_item_id = response.json()["setItem"]["Id"]
            if set_item.set_key > 0:
                response = self.session.put(self.base_url + "/api/arrange/setItem", headers=self.headers, json=[{"id": set_item_id, "data": {"keyOfset": set_item.key_offset()}}])

    def set_headers(self):
        print('Waiting for approval from application...')
        self.session.get(self.base_url + "/api/editor/songs")
        cookies = self.session.cookies.get_dict()
        self.cookie = cookies['jagses']
        self.headers = {"Cookie": f"jagses={self.cookie}"}