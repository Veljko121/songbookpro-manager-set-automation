from song import Song
from sqlite3 import Connection
from base_song_repository import BaseSongRepository

class DatabaseSongRepository(BaseSongRepository):

    def __init__(self, database_client: Connection):
        self.database = database_client

    def find_by_name(self, name: str) -> Song:
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM songs WHERE name = ? OR subTitle = ? OR name || ' (' || author || ')' = ?", (name, name, name))
        row = cursor.fetchone()
        cursor.close()
        return self._map_row_to_song(row) if row else None
    
    def _map_row_to_song(self, row):
        dict_row = dict(row)
        song = Song(
            dict_row["Id"],
            dict_row["name"],
            dict_row["author"],
            dict_row["key"],
            dict_row["subTitle"],
            dict_row["KeyShift"],
        )
        return song