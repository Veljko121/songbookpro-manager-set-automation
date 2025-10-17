from sqlite3 import Connection, Cursor
from set import Set

class DatabaseSetRepository:

    def __init__(self, database_client: Connection):
        self.database = database_client

    def save(self, set: Set):
        cursor = self.database.cursor()
        try:
            cursor.execute("INSERT INTO sets(name, date, ModifiedDateTime) VALUES (?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))", (set.name, ))
            self._save_set_items(set.items, cursor)
            self.database.commit()
        finally:
            cursor.close()

    def _save_set_items(set_items: list, cursor: Cursor):
        set_id = cursor.lastrowid
        values = [(0, order, set_id, item.song.id, item.key_offset()) for order, item in enumerate(set.items)]
        cursor.executemany("INSERT INTO setitems(Capo, \"Order\", SetId, SongId, keyOfset, ModifiedDateTime)VALUES (?, ?, ?, ?, ?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))", values)
