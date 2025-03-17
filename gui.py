from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QRect, QCoreApplication, QMetaObject
import sys

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

        self.sheetNameLineEdit = QLineEdit(CreateSet)
        self.sheetNameLineEdit.setObjectName(u"sheetNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sheetNameLineEdit)

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
            self.ui.spreadsheetPathLineEdit.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateSet()
    window.show()
    sys.exit(app.exec())

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     AddLokalDialog = QDialog()
#     ui = Ui_CreateSet()
#     ui.setupUi(AddLokalDialog)
#     AddLokalDialog.show()
#     sys.exit(app.exec())
