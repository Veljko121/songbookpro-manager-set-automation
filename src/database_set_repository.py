from sqlite3 import Connection
from set import Set
from base_set_repository import BaseSetRepository

class DatabaseSetRepository(BaseSetRepository):

    def __init__(self, database_client: Connection):
        self.database = database_client

    def save(self, set: Set):
        cursor = self.database.cursor()
        try:
            cursor.execute("INSERT INTO sets(name, date, ModifiedDateTime) VALUES (?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'), strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))", (set.name, ))

            # Save set items
            set_id = cursor.lastrowid
            values = [(0, order, set_id, item.song.id, item.key_offset(), item.notes) for order, item in enumerate(set.items)]
            cursor.executemany("INSERT INTO setitems(Capo, \"Order\", SetId, SongId, keyOfset, NotesText, ModifiedDateTime)VALUES (?, ?, ?, ?, ?, ?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))", values)

            self.database.commit()
        finally:
            cursor.close()
