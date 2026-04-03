import gspread
from base_repertoire_repository import BaseRepertoireRepository
from typing import List, Tuple

class GoogleSheetsRepertoireRepository(BaseRepertoireRepository):

    def __init__(self, google_sheets_client: gspread.client.Client, google_spreadsheet_id: str, google_sheet: str):
        super().__init__()
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