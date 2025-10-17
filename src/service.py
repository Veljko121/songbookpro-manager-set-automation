from google_sheets_repertoire_repository import GoogleSheetsRepertoireRepository

class Service:

    # 1. UI: I want a Google Sheets reader. Here's necessary stuff (path to credentials, URL, sheet name)
    # 2. Backend: Okay, let me check if that is possible
    #       - credentials good?
    #           - yes
    #    Okay, let me get all songs from the spreadsheet

    # 1. load song names from the repertoire
    # 2. find songs from the database by those names (check if each one exists)

    def create_set(self, sheets_selection: int, sheets_params: dict, database_selection: int, database_params):
        if sheets_selection == 0:
            self.repertoire_repository = GoogleSheetsRepertoireRepository(sheets_params["credentials_path"], sheets_params["spreadsheet_url"], sheets_params["sheet"])
        elif sheets_selection == 1:
            pass
        else:
            raise ValueError(f"Sheets method selection not valid - selected {sheets_selection}. Value should be either 0 or 1.")
        

        
if __name__ == "__main__":
    service = Service()
    sheets_selection = 0
    sheets_params = {
        "credentials_path": "resources/credentials.json",
        "spreadsheet_url": "https://docs.google.com/spreadsheets/d/1Sx-4TBd1RZTSTZj4V9cFGHGp50JtzlnsLb8UixmIy7U/edit?gid=1836157840#gid=1836157840",
        "sheet": "Cohiba"
    }
    service.create_set(sheets_selection, sheets_params, None, None)