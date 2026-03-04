from song import Song
from sqlite3 import Connection

class DatabaseSongRepository:

    def __init__(self, database_client: Connection):
        self.database = database_client

    def find_by_name(self, name: str):
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM songs WHERE name = ? OR subTitle = ?", (name, name))
        row = cursor.fetchone()
        cursor.close()
        return self._map_row_to_song(row) if row else None
    
    def find_all_by_names(self, names: list):
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
    
    def _map_row_to_song(self, row):
        dict_row = dict(row)
        song = Song(
            dict_row["Id"],
            dict_row["name"],
            dict_row["key"],
            dict_row["subTitle"],
            dict_row["KeyShift"],
        )
        return song