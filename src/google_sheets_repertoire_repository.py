import gspread

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

    def __init__(self, credentials_path: str, spreadsheet_url: str, sheet: str):
        self.client = gspread.auth.service_account(credentials_path)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)
        self.sheet = self.spreadsheet.worksheet(sheet)

    def get_songs(self, songs_column: int = 1):
        return [
            (format_song_name(song_name), keys[key]) 
            for song_name, key
            in zip(self.sheet.col_values(songs_column), self.sheet.col_values(songs_column + 1))
        ]