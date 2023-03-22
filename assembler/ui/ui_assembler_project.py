# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_assembler_project.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateProject(object):
    def setupUi(self, CreateProject):
        if not CreateProject.objectName():
            CreateProject.setObjectName(u"CreateProject")
        CreateProject.resize(400, 160)
        self.verticalLayout = QVBoxLayout(CreateProject)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_5 = QSplitter(CreateProject)
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

        self.splitter = QSplitter(CreateProject)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.splitter.addWidget(self.label)
        self.linSizeX = QLineEdit(self.splitter)
        self.linSizeX.setObjectName(u"linSizeX")
        self.splitter.addWidget(self.linSizeX)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(CreateProject)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.splitter_2.addWidget(self.label_2)
        self.linSizeY = QLineEdit(self.splitter_2)
        self.linSizeY.setObjectName(u"linSizeY")
        self.splitter_2.addWidget(self.linSizeY)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_4 = QSplitter(CreateProject)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(150, 16777215))
        self.splitter_4.addWidget(self.label_4)
        self.linDescription = QLineEdit(self.splitter_4)
        self.linDescription.setObjectName(u"linDescription")
        self.splitter_4.addWidget(self.linDescription)

        self.verticalLayout.addWidget(self.splitter_4)

        self.btnCreateProject = QPushButton(CreateProject)
        self.btnCreateProject.setObjectName(u"btnCreateProject")
        self.btnCreateProject.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btnCreateProject)


        self.retranslateUi(CreateProject)

        QMetaObject.connectSlotsByName(CreateProject)
    # setupUi

    def retranslateUi(self, CreateProject):
        CreateProject.setWindowTitle(QCoreApplication.translate("CreateProject", u"Create Project", None))
        self.btnPickProject.setText(QCoreApplication.translate("CreateProject", u"Pick Project Folder", None))
        self.label.setText(QCoreApplication.translate("CreateProject", u"Resolution X", None))
        self.label_2.setText(QCoreApplication.translate("CreateProject", u"Resolution Y", None))
        self.label_4.setText(QCoreApplication.translate("CreateProject", u"Description", None))
        self.btnCreateProject.setText(QCoreApplication.translate("CreateProject", u"Create Project", None))
    # retranslateUi

