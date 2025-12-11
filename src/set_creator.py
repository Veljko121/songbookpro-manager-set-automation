from ui.ui_set_creator import Ui_SetCreator
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt6.QtGui import QKeySequence, QShortcut
from service import Service


class SetCreator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_SetCreator()
        self.ui.setupUi(self)

        # Ctrl+Q shortcut
        shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut.activated.connect(self.close)

        # Service initialization
        self.service = Service()

        # Signals setup
        self._connect_actions()

        self.adjustSize()

    def _connect_actions(self):
        self.ui.browseCredentialsPushButton.clicked.connect(self.browse_credentials)
        self.ui.googleSpreadsheetsComboBox.currentIndexChanged.connect(self.update_google_sheets)

        self.ui.browseLocalDatabasePushButton.clicked.connect(self.browse_sqlite_database)

        self.ui.createSetpushButton.clicked.connect(self.create_set)

    def browse_credentials(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open credentials", "./resources/credentials", "Credentials JSON (*.json)")
        if file_path:
            self.ui.credentialsPathLineEdit.setText(file_path)
            spreadsheets = self.service.get_available_google_spreadsheets(self.ui.credentialsPathLineEdit.text())
            self.ui.googleSpreadsheetsComboBox.clear()
            for spreadsheet in spreadsheets:
                self.ui.googleSpreadsheetsComboBox.addItem(spreadsheet.title, spreadsheet.id)
    
    def update_google_sheets(self):
        self.ui.googleSheetsComboBox.clear()
        sheets = self.service.get_sheets(self.ui.repertoireTabWidget.currentIndex(), { "spreadsheet_id": self.ui.googleSpreadsheetsComboBox.currentData() })
        for sheet in sheets:
            self.ui.googleSheetsComboBox.addItem(sheet.title, sheet.id)

    def browse_sqlite_database(self):
        database_path, _ = QFileDialog.getOpenFileName(self, "Open local database", "/home/veljko/.wine/drive_c/users/veljko/AppData/Roaming/Songbook Systems/SongbookPro", "Database (*.db)")
        if database_path:
            self.ui.localDatabasePathLineEdit.setText(database_path)
        
    def create_set(self):
        sheets_selection = self.ui.repertoireTabWidget.currentIndex()
        sheets_params = {
            "credentials_path": self.ui.credentialsPathLineEdit.text(),
            "spreadsheet_id": self.ui.googleSpreadsheetsComboBox.currentData(),
            "sheet": self.ui.googleSheetsComboBox.currentText(),
        }
        database_selection =self.ui.databaseTabWidget.currentIndex()
        database_params = {
            "database_path": self.ui.localDatabasePathLineEdit.text()
        }
        set_name = self.ui.setNameLineEdit.text()
        self.service.create_set(sheets_selection, sheets_params, database_selection, database_params, set_name)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    setCreator = SetCreator()
    setCreator.show()
    sys.exit(app.exec())
