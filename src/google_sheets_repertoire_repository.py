import gspread

class GoogleSheetsRepertoireRepository:

    def __init__(self, credentials_path: str, spreadsheet_url: str, sheet: str):
        self.client = gspread.auth.service_account(credentials_path)
        self.spreadsheet = self.client.open_by_url(spreadsheet_url)
        self.sheet = self.spreadsheet.worksheet(sheet)