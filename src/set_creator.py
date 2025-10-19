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
        self.ui.spreadsheetsComboBox.currentIndexChanged.connect(self.update_sheets)

    def browse_credentials(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open credentials", "", "Credentials JSON (*.json)")
        if file_path:
            self.ui.credentialsPathLineEdit.setText(file_path)
            spreadsheets = self.service.get_available_google_spreadsheets(self.ui.credentialsPathLineEdit.text())
            self.ui.spreadsheetsComboBox.clear()
            for spreadsheet in spreadsheets:
                self.ui.spreadsheetsComboBox.addItem(spreadsheet.title, spreadsheet.id)
    
    def update_sheets(self):
        self.ui.sheetsComboBox.clear()
        sheets_selection = self.ui.repertoireTabWidget.currentIndex()
        if sheets_selection == 0:
            sheets = self.service.get_sheets(self.ui.repertoireTabWidget.currentIndex(), { "spreadsheet_id": self.ui.spreadsheetsComboBox.currentData() })
            for sheet in sheets:
                self.ui.sheetsComboBox.addItem(sheet.title, sheet.id)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    setCreator = SetCreator()
    setCreator.show()
    sys.exit(app.exec())
