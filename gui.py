from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QCoreApplication, QMetaObject
import sys
from lib import run, get_sheet_names
import os

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'songbookpro-manager-set-automationYxUIbH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_CreateSet(object):
    def setupUi(self, CreateSet):
        if not CreateSet.objectName():
            CreateSet.setObjectName(u"CreateSet")
        CreateSet.resize(352, 204)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateSet.sizePolicy().hasHeightForWidth())
        CreateSet.setSizePolicy(sizePolicy)
        
        self.horizontalLayout = QHBoxLayout(CreateSet)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spreadsheetPathLabel = QLabel(CreateSet)
        self.spreadsheetPathLabel.setObjectName(u"spreadsheetPathLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.spreadsheetPathLabel)

        # Horizontal layout for file input and browse button
        self.pathLayout = QHBoxLayout()
        self.spreadsheetPathLineEdit = QLineEdit(CreateSet)
        self.spreadsheetPathLineEdit.setObjectName(u"spreadsheetPathLineEdit")
        self.pathLayout.addWidget(self.spreadsheetPathLineEdit)

        self.browseButton = QPushButton("...")
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setFixedWidth(30)
        self.pathLayout.addWidget(self.browseButton)

        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.pathLayout)

        self.sheetNameLabel = QLabel(CreateSet)
        self.sheetNameLabel.setObjectName(u"sheetNameLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.sheetNameLabel)

        # self.sheetNameLineEdit = QLineEdit(CreateSet)
        # self.sheetNameLineEdit.setObjectName(u"sheetNameLineEdit")
        self.sheetNameComboBox = QComboBox(CreateSet)
        self.sheetNameComboBox.setObjectName(u"sheetNameComboBox")
        self.sheetNameComboBox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed) 
        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sheetNameComboBox)

        self.setNameLabel = QLabel(CreateSet)
        self.setNameLabel.setObjectName(u"setNameLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.setNameLabel)

        self.setNameLineEdit = QLineEdit(CreateSet)
        self.setNameLineEdit.setObjectName(u"setNameLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.setNameLineEdit)

        self.urlLabel = QLabel(CreateSet)
        self.urlLabel.setObjectName(u"urlLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.urlLabel)

        self.urlHorizontalLayout = QHBoxLayout()
        self.urlHorizontalLayout.setObjectName(u"urlHorizontalLayout")
        self.httpLabel = QLabel(CreateSet)
        self.httpLabel.setObjectName(u"httpLabel")

        self.urlHorizontalLayout.addWidget(self.httpLabel)

        self.ipAddressLineEdit = QLineEdit(CreateSet)
        self.ipAddressLineEdit.setObjectName(u"ipAddressLineEdit")

        self.urlHorizontalLayout.addWidget(self.ipAddressLineEdit)

        self.portLabel = QLabel(CreateSet)
        self.portLabel.setObjectName(u"portLabel")

        self.urlHorizontalLayout.addWidget(self.portLabel)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.urlHorizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.createSetPushButton = QPushButton(CreateSet)
        self.createSetPushButton.setObjectName(u"createSetPushButton")

        self.verticalLayout.addWidget(self.createSetPushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(CreateSet)

        QMetaObject.connectSlotsByName(CreateSet)
    # setupUi

    def retranslateUi(self, CreateSet):
        CreateSet.setWindowTitle(QCoreApplication.translate("CreateSet", u"Create set", None))
        self.spreadsheetPathLabel.setText(QCoreApplication.translate("CreateSet", u"Spreadsheet path", None))
        self.sheetNameLabel.setText(QCoreApplication.translate("CreateSet", u"Sheet name", None))
        self.setNameLabel.setText(QCoreApplication.translate("CreateSet", u"Set name", None))
        self.urlLabel.setText(QCoreApplication.translate("CreateSet", u"URL", None))
        self.httpLabel.setText(QCoreApplication.translate("CreateSet", u"http://", None))
        self.portLabel.setText(QCoreApplication.translate("CreateSet", u":8080", None))
        self.createSetPushButton.setText(QCoreApplication.translate("CreateSet", u"Create set", None))
    # retranslateUi


class CreateSet(QWidget):
    def __init__(self):
        super(CreateSet, self).__init__()
        self.ui = Ui_CreateSet()
        self.ui.setupUi(self)
        self.adjustSize()
        self.setFixedHeight(self.height())
        self.ui.browseButton.clicked.connect(self.open_file_dialog)
        self.ui.createSetPushButton.clicked.connect(self.create_set)
        self.ui.sheetNameComboBox.setEnabled(False)
        self.ui.spreadsheetPathLineEdit.editingFinished.connect(self.update_sheets)
        self.load_cache()

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Spreadsheet", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.ui.spreadsheetPathLineEdit.setText(file_path)
            self.update_sheets()

    def update_sheets(self):
        # Try to load sheet names
        try:
            sheets = get_sheet_names(self.ui.spreadsheetPathLineEdit.text())  # Get sheet names
            self.ui.sheetNameComboBox.clear()  # Clear previous entries
            self.ui.sheetNameComboBox.addItems(sheets)  # Add new sheet names
            self.ui.sheetNameComboBox.setEnabled(True)  # Enable the combo box
        except Exception as e:
            if self.ui.spreadsheetPathLineEdit.text():
                self.show_error_message(f"Failed to read spreadsheet: {e}")
            
            self.ui.sheetNameComboBox.clear()
            self.ui.sheetNameComboBox.setEnabled(False)

    def create_set(self):
        ipAddress = self.ui.ipAddressLineEdit.text()
        spreadsheet = self.ui.spreadsheetPathLineEdit.text()
        sheet = self.ui.sheetNameComboBox.currentText()
        set_name = self.ui.setNameLineEdit.text()

        try:
            run(ipAddress, spreadsheet, sheet, set_name)
            self.save_to_properties(ipAddress, spreadsheet, sheet, set_name)
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Information)  # Use Critical icon for errors
            msg_box.setWindowTitle("Success")
            msg_box.setText(f"Set {set_name} created successfully.")
            msg_box.exec()
        except ValueError as e:
            self.show_error_message(str(e))
        except FileNotFoundError:
            self.show_error_message("Spreadsheet '" + spreadsheet + "' doesn't seem to exist. Try again.")
        except KeyError:
            self.show_error_message("Worksheet '" + sheet + "' doesn't seem to exist. Try again.")
            
    def show_error_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)  # Use Critical icon for errors
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()

    def save_to_properties(self, ipAddress, spreadsheet, sheet, set_name):
        # Set the hidden .properties file path
        properties_file = "application.properties"

        # Prepare the content
        properties_content = f"IP_ADDRESS={ipAddress}\nSPREADSHEET_PATH={spreadsheet}\nSHEET={sheet}\nSET_NAME={set_name}"

        # Write the data to the .properties file
        with open(properties_file, "w") as file:
            file.write(properties_content)

    def load_cache(self):
        properties_file = "application.properties"

        if os.path.exists(properties_file):
            try:
                with open(properties_file, "r") as file:
                    # Read and split the file content line by line
                    properties = {}
                    for line in file.readlines():
                        key, value = line.strip().split("=", 1)
                        properties[key] = value

                    # Set the values to the UI elements
                    self.ui.ipAddressLineEdit.setText(properties.get("IP_ADDRESS", ""))
                    self.ui.spreadsheetPathLineEdit.setText(properties.get("SPREADSHEET_PATH", ""))
                    self.update_sheets()
                    self.ui.sheetNameComboBox.setCurrentText(properties.get("SHEET", ""))
                    self.ui.setNameLineEdit.setText(properties.get("SET_NAME", ""))

            except Exception as e:
                self.show_error_message(f"Failed to load properties: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateSet()
    window.show()
    sys.exit(app.exec())
