import gspread
from base_repertoire_repository import BaseRepertoireRepository
from typing import List, Tuple

class GoogleSheetsRepertoireRepository(BaseRepertoireRepository):

    def __init__(self, google_sheets_client: gspread.client.Client):
        super().__init__()
        self.client = google_sheets_client

    def get_available_spreadsheets(self):
        return self.client.openall()
    
    def get_sheets(self, spreadsheet_id: str):
        return self.client.open_by_key(spreadsheet_id).worksheets()

    def _fetch_songs(self, spreadsheet_id: str, sheet_id: str, song_names_column: int, keys_column: int, notes_column: int) -> Tuple[List[str], List[str], List[str]]:
        worksheet = self.client.open_by_key(spreadsheet_id).worksheet(sheet_id)
        song_names = worksheet.col_values(song_names_column)
        song_keys = worksheet.col_values(keys_column)
        song_notes = worksheet.col_values(notes_column)
        return song_names, song_keys, song_notes
    
if __name__ == "__main__":
    google_sheets_client = gspread.auth.service_account("./resources/credentials/credentials.json")
    repo = GoogleSheetsRepertoireRepository(google_sheets_client)
    songs = repo.get_songs("1Sx-4TBd1RZTSTZj4V9cFGHGp50JtzlnsLb8UixmIy7U", "Pub 21465", 1, 2, 3)