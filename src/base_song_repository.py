from abc import ABC, abstractmethod
from song import Song
from typing import List

class BaseSongRepository(ABC):

    @abstractmethod
    def find_by_name(self, name: str) -> Song:
        pass

    def find_all_by_names(self, names: List[str]) -> List[Song]:
        songs = []
        not_found = []
        for name in names:
            song = self.find_by_name(name)
            if song is None:
                not_found.append(name)
            else:
                songs.append(song)
        if len(not_found) > 0:
            raise ValueError(f"Songs: {not_found} have not been found.")
        return songs