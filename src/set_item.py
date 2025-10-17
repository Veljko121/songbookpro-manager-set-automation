from song import Song

class SetItem:
    
    def __init__(self, song: Song, set_key: int):
        self.song = song
        self.set_key = set_key

    def key_offset(self):
        distance = 12 - (self.song.key - self.set_key) if self.song.key > self.set_key else self.set_key - self.song.key
        return distance