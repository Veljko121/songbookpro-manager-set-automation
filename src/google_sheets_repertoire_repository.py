import gspread
from set_item import SetItem

def format_song_name(name: str):
    return name.strip().replace("‘", "'").replace("’", "'")

class GoogleSheetsRepertoireRepository:

    def __init__(self, credentials_path: str, spreadsheet_url: str, sheet: str):
        self.client = gspread.auth.service_account(credentials_path)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)
        self.sheet = self.spreadsheet.worksheet(sheet)

    def get_songs(self, songs_column: int = 1):
        return [
            (format_song_name(song_name), key) 
            for song_name, key
            in zip(self.sheet.col_values(songs_column), self.sheet.col_values(songs_column + 1))
        ]