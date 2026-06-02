from ui.ui_set_creator import Ui_SetCreator
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PyQt6.QtGui import QKeySequence, QShortcut
from service import Service
from properties_handler import PropertiesHandler
import os


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

        # Properties handler
        self.properties_handler = PropertiesHandler()
        self._load_properties()

        # Columns set up
        self.ui.columnDefinitionSongNamesSpinBox.setValue(1)
        self.ui.columnDefinitionKeysSpinBox.setValue(2)
        self.ui.columnDefinitionNotesSpinBox.setValue(3)

        self.adjustSize()

    def _connect_actions(self):
        # Google Sheets actions
        self.ui.browseCredentialsPushButton.clicked.connect(self.browse_credentials)
        self.ui.googleSpreadsheetsComboBox.currentIndexChanged.connect(self.update_google_sheets)
        self.ui.reloadGoogleSheetsPushButton.clicked.connect(lambda: self._load_credentials(self.ui.credentialsPathLineEdit.text()))

        # Local spreadsheets actions
        self.ui.browseSpreadsheetsPushButton.clicked.connect(self.browse_local_spreadsheet)
        self.ui.spreadsheetPathLineEdit.textChanged.connect(self.update_local_sheets)

        # Local database actions
        self.ui.browseLocalDatabasePushButton.clicked.connect(self.browse_sqlite_database)

        # Create set button
        self.ui.createSetPushButton.clicked.connect(self.create_set)

    def _load_properties(self):

        credentials_path = self.properties_handler.get_property("GOOGLE_CREDENTIALS_PATH")
        if os.path.isfile(credentials_path):
            self.ui.credentialsPathLineEdit.setText(credentials_path)
        else:
            self.properties_handler.delete_property("GOOGLE_CREDENTIALS_PATH")
        # self._load_credentials(credentials_path)
        # self.ui.googleSheetsComboBox.setCurrentText(self.properties_handler.get_property("GOOGLE_SHEET"))
        # self.ui.googleSpreadsheetsComboBox.setCurrentText(self.properties_handler.get_property("GOOGLE_SPREADSHEETS"))

        local_spreadsheet_path = self.properties_handler.get_property("LOCAL_SPREADSHEET_PATH")
        if os.path.isfile(local_spreadsheet_path):
            self.ui.spreadsheetPathLineEdit.setText(local_spreadsheet_path)
            self.ui.localSheetsComboBox.setCurrentText(self.properties_handler.get_property("LOCAL_SHEET"))
        else:
            self.properties_handler.delete_property("LOCAL_SPREADSHEET_PATH")

        self.ui.columnDefinitionSongNamesSpinBox.setValue(int(self.properties_handler.get_property("SONG_NAMES_COLUMN") if self.properties_handler.get_property("SONG_NAMES_COLUMN") else 1))
        self.ui.columnDefinitionKeysSpinBox.setValue(int(self.properties_handler.get_property("KEYS_COLUMN") if self.properties_handler.get_property("KEYS_COLUMN") else 2))
        self.ui.columnDefinitionNotesSpinBox.setValue(int(self.properties_handler.get_property("NOTES_COLUMN") if self.properties_handler.get_property("NOTES_COLUMN") else 3))

        local_database_path = self.properties_handler.get_property("LOCAL_DATABASE_PATH")
        if os.path.isfile(local_database_path):
            self.ui.localDatabasePathLineEdit.setText(self.properties_handler.get_property("LOCAL_DATABASE_PATH"))
        else:
            self.properties_handler.delete_property("LOCAL_DATABASE_PATH")

        self.ui.ipAddressLineEdit.setText(self.properties_handler.get_property("SONGBOOKPRO_MANAGER_IP_ADDRESS"))
        self.ui.portLineEdit.setText(self.properties_handler.get_property("SONGBOOKPRO_MANAGER_PORT"))

        self.ui.setNameLineEdit.setText(self.properties_handler.get_property("SET_NAME"))

    def browse_credentials(self):
        cached_path: str = self.properties_handler.get_property("GOOGLE_CREDENTIALS_PATH")
        path = cached_path if cached_path else os.path.expanduser("~")
        file_path, _ = QFileDialog.getOpenFileName(self, "Open credentials", path, "Credentials JSON (*.json)")
        self._load_credentials(file_path)

    def _load_credentials(self, credentials_path: str):
        if credentials_path:
            self.ui.credentialsPathLineEdit.setText(credentials_path)
            spreadsheets = self.service.get_available_google_spreadsheets(self.ui.credentialsPathLineEdit.text())
            self.ui.googleSpreadsheetsComboBox.clear()
            for spreadsheet in spreadsheets:
                self.ui.googleSpreadsheetsComboBox.addItem(spreadsheet.title, spreadsheet.id)
    
    def update_google_sheets(self):
        self.ui.googleSheetsComboBox.clear()
        sheets = self.service.get_sheets(0, self.ui.googleSpreadsheetsComboBox.currentData())
        for sheet in sheets:
            self.ui.googleSheetsComboBox.addItem(sheet.title, sheet.id)

    def browse_local_spreadsheet(self):
        cached_path: str = self.properties_handler.get_property("LOCAL_SPREADSHEET_PATH")
        path = cached_path if cached_path else os.path.expanduser("~")
        file_path, _ = QFileDialog.getOpenFileName(self, "Open local spreadsheet", path, "Microsoft  Excel (*.xlsx)")
        self._load_local_spreadsheet(file_path)

    def _load_local_spreadsheet(self, local_spreadsheet_path: str):
        if local_spreadsheet_path:
            self.ui.spreadsheetPathLineEdit.setText(local_spreadsheet_path)
    
    def update_local_sheets(self):
        self.ui.localSheetsComboBox.clear()
        sheets = self.service.get_sheets(1, self.ui.spreadsheetPathLineEdit.text())
        self.ui.localSheetsComboBox.addItems(sheets)

    def browse_sqlite_database(self):
        database_path, _ = QFileDialog.getOpenFileName(self, "Open local database", "/home/veljko/.wine/drive_c/users/veljko/AppData/Roaming/Songbook Systems/SongbookPro", "Database (*.db)")
        if database_path:
            self.ui.localDatabasePathLineEdit.setText(database_path)
        
    def create_set(self):
        try:
            # sheets config
            sheets_selection = self.ui.repertoireTabWidget.currentIndex()
            song_names_column = int(self.ui.columnDefinitionSongNamesSpinBox.text())
            keys_column = int(self.ui.columnDefinitionKeysSpinBox.text())
            notes_column = int(self.ui.columnDefinitionNotesSpinBox.text())
            self._validate_column_parameters(song_names_column, keys_column, notes_column)
            sheets_params = {
                "google_credentials_path": self.ui.credentialsPathLineEdit.text(),
                "google_spreadsheet_id": self.ui.googleSpreadsheetsComboBox.currentData(),
                "google_sheet": self.ui.googleSheetsComboBox.currentText(),
                "local_spreadsheet_path": self.ui.spreadsheetPathLineEdit.text(),
                "local_sheet": self.ui.localSheetsComboBox.currentText(),
                "song_names_column": song_names_column,
                "keys_column": keys_column,
                "notes_column": notes_column,
            }

            # database config
            database_selection = self.ui.databaseTabWidget.currentIndex()
            database_params = {
                "local_database_path": self.ui.localDatabasePathLineEdit.text(),
                "songbookpro_manager_ip_address": self.ui.ipAddressLineEdit.text(),
                "songbookpro_manager_port": self.ui.portLineEdit.text(),
            }

            # set config
            set_name = self.ui.setNameLineEdit.text()

            self.service.create_set(sheets_selection, sheets_params, database_selection, database_params, set_name)
            self.show_message(QMessageBox.Icon.Information, "Success", f"Set '{set_name}' created successfully.")
        except ValueError as e:
            self.show_message(QMessageBox.Icon.Critical, "Error", str(e))
    
    def _validate_column_parameters(self, song_names_column: int, keys_column: int, notes_column: int):
        """Validate that column parameters are valid."""
        if song_names_column <= 0:
            raise ValueError(f"Song names column value must be greater than 0 ({song_names_column}).")
        if keys_column <= 0:
            raise ValueError(f"Keys column value must be greater than 0 ({keys_column}).")
        if notes_column <= 0:
            raise ValueError(f"Notes column value must be greater than 0 ({notes_column}).")
        if song_names_column == keys_column:
            raise ValueError(f"Song names column value ({song_names_column}) and keys column value ({keys_column}) cannot be the same.")
        if song_names_column == notes_column:
            raise ValueError(f"Song names column value ({song_names_column}) and notes column value ({notes_column}) cannot be the same.")
        if keys_column == notes_column:
            raise ValueError(f"Keys column value ({keys_column}) and notes column value ({notes_column}) cannot be the same.")

    def show_message(self, message_type: QMessageBox.Icon, message_title: str, message_content: str):
        msg_box = QMessageBox(self)
        msg_box.setIcon(message_type)
        msg_box.setWindowTitle(message_title)
        msg_box.setText(message_content)
        msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    setCreator = SetCreator()
    setCreator.show()
    sys.exit(app.exec())
