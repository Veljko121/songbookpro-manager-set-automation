from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog, QComboBox
)
import sys

class SpreadsheetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.adjustSize()

    def initUI(self):
        layout = QVBoxLayout()

        # Spreadsheet Path
        path_layout = QHBoxLayout()
        self.path_label = QLabel("Spreadsheet path:")
        self.path_input = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.open_file_dialog)

        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.browse_button)

        # Sheet Selection
        sheet_layout = QHBoxLayout()
        self.sheet_label = QLabel("Sheet:")
        self.sheet_input = QLineEdit()

        sheet_layout.addWidget(self.sheet_label)
        sheet_layout.addWidget(self.sheet_dropdown)

        # Add layouts to main layout
        layout.addLayout(path_layout)
        layout.addLayout(sheet_layout)

        self.setLayout(layout)
        self.setWindowTitle("Spreadsheet Selector")

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Spreadsheet", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.path_input.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpreadsheetApp()
    window.show()
    sys.exit(app.exec())
