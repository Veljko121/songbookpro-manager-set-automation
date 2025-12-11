import sqlite3
from google_sheets_repertoire_repository import GoogleSheetsRepertoireRepository
from database_song_repository import DatabaseSongRepository
from database_set_repository import DatabaseSetRepository
from set_item import SetItem
from set import Set
import gspread

class Service:

    def __init__(self):
        self.credentials_path = None
        self.google_sheets_client = None

    def get_available_google_spreadsheets(self, credentials_path: str):
        if self.credentials_path and self.credentials_path != credentials_path:
            self.credentials_path = credentials_path
        if not self.google_sheets_client:
            self.google_sheets_client = gspread.auth.service_account(credentials_path)
        self.google_sheets_repertoire_repository = GoogleSheetsRepertoireRepository(self.google_sheets_client)
        return self.google_sheets_repertoire_repository.get_available_spreadsheets()
    
    def get_sheets(self, sheets_selection: int, sheets_params: dict):
        if sheets_selection == 0:
            return self.google_sheets_repertoire_repository.get_sheets(sheets_params["spreadsheet_id"])

    def create_set(self, sheets_selection: int, sheets_params: dict, database_selection: int, database_params: dict, set_name: str):
        # self.repertoire_repository = self._initialize_repertoire_repository(sheets_selection, sheets_params)
        self.song_repository, self.set_repository = self._initialize_database_repositories(database_selection, database_params)

        repertoire_songs = self.google_sheets_repertoire_repository.get_songs(sheets_params["spreadsheet_id"], sheets_params["sheet"])
        songs = self.song_repository.find_all_by_names([repertoire_song[0] for repertoire_song in repertoire_songs])
        set_items = [SetItem(song, repertoire_song[1]) for (song, repertoire_song) in zip(songs, repertoire_songs)]
        set = Set(set_name, set_items)
        self.set_repository.save(set)

    def _initialize_repertoire_repository(self, sheets_selection: int, sheets_params: dict):
        if sheets_selection == 0: # Google Sheets
            repertoire_repository = GoogleSheetsRepertoireRepository(sheets_params["credentials_path"], sheets_params["spreadsheet_id"], sheets_params["sheet"])
            return repertoire_repository
        elif sheets_selection == 1: # Local spreadsheets
            pass # TODO
        else:
            raise ValueError(f"Sheets method selection not valid - selected {sheets_selection}. Value should be either 0 or 1.")
    
    def _initialize_database_repositories(self, database_selection: int, database_params):
        if database_selection == 0: # SQLite database
            database_client = sqlite3.connect(database_params["database_path"])
            database_client.row_factory = sqlite3.Row
            song_repository = DatabaseSongRepository(database_client)
            set_repository = DatabaseSetRepository(database_client)
            return song_repository, set_repository
        elif database_selection == 1: # SongbookPro Manager
            pass # TODO
        else:
            raise ValueError(f"Database method selection not valid - selected {database_selection}. Value should be either 0 or 1.")

        
if __name__ == "__main__":
    service = Service()
    sheets_selection = 0
    database_selection = 0
    sheets_params = {
        "credentials_path": "resources/credentials/credentials.json",
        "spreadsheet_id": "https://docs.google.com/spreadsheets/d/1Sx-4TBd1RZTSTZj4V9cFGHGp50JtzlnsLb8UixmIy7U/edit?gid=1836157840#gid=1836157840",
        "sheet": "Cohiba"
    }
    database_params = {
        "database_path": "/home/veljko/.wine/drive_c/users/veljko/AppData/Roaming/Songbook Systems/SongbookPro/songs.db"
    }
    service.create_set(sheets_selection, sheets_params, database_selection, database_params, "Pub 21465")