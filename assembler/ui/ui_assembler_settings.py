# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_assembler_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 186)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_5 = QSplitter(Settings)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.btnPickProject = QPushButton(self.splitter_5)
        self.btnPickProject.setObjectName(u"btnPickProject")
        self.btnPickProject.setMinimumSize(QSize(150, 0))
        self.btnPickProject.setMaximumSize(QSize(150, 16777215))
        self.splitter_5.addWidget(self.btnPickProject)
        self.linProjectFolder = QLineEdit(self.splitter_5)
        self.linProjectFolder.setObjectName(u"linProjectFolder")
        self.splitter_5.addWidget(self.linProjectFolder)

        self.verticalLayout.addWidget(self.splitter_5)

        self.splitter = QSplitter(Settings)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.splitter.addWidget(self.label)
        self.linVersionedPages = QLineEdit(self.splitter)
        self.linVersionedPages.setObjectName(u"linVersionedPages")
        self.splitter.addWidget(self.linVersionedPages)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(Settings)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.splitter_2.addWidget(self.label_2)
        self.linFinalPages = QLineEdit(self.splitter_2)
        self.linFinalPages.setObjectName(u"linFinalPages")
        self.splitter_2.addWidget(self.linFinalPages)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(Settings)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.splitter_3.addWidget(self.label_3)
        self.linPDFfiles = QLineEdit(self.splitter_3)
        self.linPDFfiles.setObjectName(u"linPDFfiles")
        self.splitter_3.addWidget(self.linPDFfiles)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(Settings)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(150, 16777215))
        self.splitter_4.addWidget(self.label_4)
        self.linSQLfile = QLineEdit(self.splitter_4)
        self.linSQLfile.setObjectName(u"linSQLfile")
        self.splitter_4.addWidget(self.linSQLfile)

        self.verticalLayout.addWidget(self.splitter_4)

        self.btnSaveSettings = QPushButton(Settings)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        self.btnSaveSettings.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btnSaveSettings)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Edit Settings", None))
        self.btnPickProject.setText(QCoreApplication.translate("Settings", u"Pick Project Folder", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Versioned Pages", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Final Pages", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"PDF files", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"SQL file", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("Settings", u"Save Settings", None))
    # retranslateUi

