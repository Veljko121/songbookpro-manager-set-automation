import gspread
from base_repertoire_repository import BaseRepertoireRepository
from typing import List, Tuple

keys = {
    "A"  :  0,
    "B"  :  1,
    "H"  :  2,
    "C"  :  3,
    "Db" :  4, "C#" :  4,
    "D"  :  5,
    "Eb" :  6, "D#" :  6,
    "E"  :  7,
    "F"  :  8,
    "F#" :  9, "Gb" :  9,
    "G"  : 10,
    "Ab" : 11, "G#" : 11, 
    "F#m": 12, "Gbm": 12,
    "Gm" : 13,
    "G#m": 14, "Abm": 14,
    "Am" : 15,
    "Bm" : 16,
    "Hm" : 17,
    "Cm" : 18,
    "C#m": 19, "Dbm": 19,
    "Dm" : 20,
    "D#m": 21, "Ebm": 21,
    "Em" : 22,
    "Fm" : 23,

    "None" : -1,
}

def format_song_name(name: str):
    return name.strip().replace("‘", "'").replace("’", "'")

class GoogleSheetsRepertoireRepository(BaseRepertoireRepository):

    def __init__(self, google_sheets_client: gspread.client.Client, google_spreadsheet_id: str, google_sheet: str):
        self.client = google_sheets_client
        self.google_spreadsheet_id = google_spreadsheet_id
        self.google_sheet = google_sheet

    def get_available_spreadsheets(self):
        return self.client.openall()
    
    def get_sheets(self, spreadsheet_id: str):
        return self.client.open_by_key(spreadsheet_id).worksheets()

    def _fetch_columns(self, song_names_column: int, keys_column: int, notes_column: int) -> Tuple[List[str], List[str], List[str]]:
        worksheet = self.client.open_by_key(self.google_spreadsheet_id).worksheet(self.google_sheet)
        song_names = worksheet.col_values(song_names_column)
        song_keys = worksheet.col_values(keys_column)
        song_notes = worksheet.col_values(notes_column)
        return song_names, song_keys, song_notes
    
if __name__ == "__main__":
    google_sheets_client = gspread.auth.service_account("./resources/credentials/credentials.json")
    repo = GoogleSheetsRepertoireRepository(google_sheets_client, "1Sx-4TBd1RZTSTZj4V9cFGHGp50JtzlnsLb8UixmIy7U", "Pub 21465")
    songs = repo.get_songs(1, 2, 3)