import sqlite3
from song import Song

class DatabaseSongRepository:

    def __init__(self, database_path: str):
        self.database = sqlite3.connect(database_path)
        self.database.row_factory = sqlite3.Row

    def find_by_name(self, name: str):
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM songs WHERE name = ? OR subTitle = ?", (name, name))
        row = cursor.fetchone()
        return self._map_row_to_song(row) if row else None
    
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