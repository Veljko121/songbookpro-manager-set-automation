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

    def __init__(self, google_sheets_client: gspread.client.Client, google_spreadsheet_id: str, google_sheet: str):
        self.client = google_sheets_client
        self.google_spreadsheet_id = google_spreadsheet_id
        self.google_sheet = google_sheet

    def get_available_spreadsheets(self):
        return self.client.openall()
    
    def get_sheets(self, spreadsheet_id: str):
        return self.client.open_by_key(spreadsheet_id).worksheets()

    def get_songs(self):
        worksheet = self.client.open_by_key(self.google_spreadsheet_id).worksheet(self.google_sheet)

        # Get all values from columns A and B
        all_values = worksheet.get('A:B')
        
        songs = []
        for row in all_values:
            # Skip empty rows
            if len(row) >= 2 and row[0] and row[1]:
                song_name = format_song_name(row[0])
                key = row[1].strip()
                songs.append((song_name, keys[key]))
        
        return songs