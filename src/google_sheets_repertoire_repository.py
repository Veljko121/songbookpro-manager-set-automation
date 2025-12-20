import gspread
from itertools import zip_longest

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

class GoogleSheetsRepertoireRepository:

    def __init__(self, google_sheets_client: gspread.client.Client, google_spreadsheet_id: str, google_sheet: str):
        self.client = google_sheets_client
        self.google_spreadsheet_id = google_spreadsheet_id
        self.google_sheet = google_sheet

    def get_available_spreadsheets(self):
        return self.client.openall()
    
    def get_sheets(self, spreadsheet_id: str):
        return self.client.open_by_key(spreadsheet_id).worksheets()

    def get_songs(self, song_names_column: int, keys_column: int):
        if song_names_column <= 0:
            raise ValueError(f"Song names column value must be greater than 0 ({song_names_column}).")
        if keys_column <= 0:
            raise ValueError(f"Keys column value must be greater than 0 ({keys_column}).")
        if song_names_column == keys_column:
            raise ValueError(f"Song names column value ({song_names_column}) and keys column value ({keys_column}) cannot be the same.")

        worksheet = self.client.open_by_key(self.google_spreadsheet_id).worksheet(self.google_sheet)
        song_names = worksheet.col_values(song_names_column)
        song_keys = worksheet.col_values(keys_column)
        
        enumerated_rows = {}
        for i, row in enumerate(zip(song_names, song_keys)):
            if row[0]:
                enumerated_rows[i] = row

        numbered_keys = []
        row_ids_with_error = []
        for id, row in enumerated_rows.items():
            try:
                numbered_keys.append(keys[row[1]])
            except KeyError:
                row_ids_with_error.append(id)
        
        if len(row_ids_with_error) > 0:
            raise ValueError(f"Key errors in rows: {[row + 1 for row in row_ids_with_error]}.")
        
        songs = []
        for id, row in enumerated_rows.items():
            # Skip rows with empty song name
            if row[0]:
                song_name = format_song_name(row[0])
                key = row[1].strip()
                songs.append((song_name, keys[key]))
        
        return songs
    
if __name__ == "__main__":
    google_sheets_client = gspread.auth.service_account("./resources/credentials/credentials.json")
    repo = GoogleSheetsRepertoireRepository(google_sheets_client, "1Sx-4TBd1RZTSTZj4V9cFGHGp50JtzlnsLb8UixmIy7U", "Pub 21465")
    songs = repo.get_songs(1, 2)