# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_assembler_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Assembler(object):
    def setupUi(self, Assembler):
        if not Assembler.objectName():
            Assembler.setObjectName(u"Assembler")
        Assembler.resize(810, 708)
        self.actionDocumentation = QAction(Assembler)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSettings = QAction(Assembler)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(Assembler)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabPages = QTableView(self.groupBox)
        self.tabPages.setObjectName(u"tabPages")

        self.verticalLayout.addWidget(self.tabPages)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.btnDownVersion = QPushButton(self.splitter)
        self.btnDownVersion.setObjectName(u"btnDownVersion")
        self.splitter.addWidget(self.btnDownVersion)
        self.btnUpVersion = QPushButton(self.splitter)
        self.btnUpVersion.setObjectName(u"btnUpVersion")
        self.splitter.addWidget(self.btnUpVersion)

        self.verticalLayout.addWidget(self.splitter)

        self.btnPublish = QPushButton(self.groupBox)
        self.btnPublish.setObjectName(u"btnPublish")

        self.verticalLayout.addWidget(self.btnPublish)

        self.btnReload = QPushButton(self.groupBox)
        self.btnReload.setObjectName(u"btnReload")

        self.verticalLayout.addWidget(self.btnReload)

        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.chbSelected = QCheckBox(self.splitter_2)
        self.chbSelected.setObjectName(u"chbSelected")
        self.chbSelected.setMaximumSize(QSize(40, 16777215))
        self.chbSelected.setChecked(True)
        self.splitter_2.addWidget(self.chbSelected)
        self.btnSendPublished = QPushButton(self.splitter_2)
        self.btnSendPublished.setObjectName(u"btnSendPublished")
        self.splitter_2.addWidget(self.btnSendPublished)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.groupBox)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.linPDFVersion = QLineEdit(self.splitter_3)
        self.linPDFVersion.setObjectName(u"linPDFVersion")
        self.linPDFVersion.setMaximumSize(QSize(40, 16777215))
        self.linPDFVersion.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.linPDFVersion)
        self.btnGeneratePDF = QPushButton(self.splitter_3)
        self.btnGeneratePDF.setObjectName(u"btnGeneratePDF")
        self.splitter_3.addWidget(self.btnGeneratePDF)

        self.verticalLayout.addWidget(self.splitter_3)


        self.horizontalLayout.addWidget(self.groupBox)

        self.grp_images = QGroupBox(self.centralwidget)
        self.grp_images.setObjectName(u"grp_images")
        self.verticalLayout_2 = QVBoxLayout(self.grp_images)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labPage = QLabel(self.grp_images)
        self.labPage.setObjectName(u"labPage")

        self.verticalLayout_2.addWidget(self.labPage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.grp_images)

        Assembler.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Assembler)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 21))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        Assembler.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Assembler)
        self.statusbar.setObjectName(u"statusbar")
        Assembler.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuEdit.addAction(self.actionSettings)

        self.retranslateUi(Assembler)

        QMetaObject.connectSlotsByName(Assembler)
    # setupUi

    def retranslateUi(self, Assembler):
        Assembler.setWindowTitle(QCoreApplication.translate("Assembler", u"Book Assembler", None))
        self.actionDocumentation.setText(QCoreApplication.translate("Assembler", u"Documentation", None))
        self.actionSettings.setText(QCoreApplication.translate("Assembler", u"Modify Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Assembler", u"Pages", None))
        self.btnDownVersion.setText(QCoreApplication.translate("Assembler", u"-", None))
        self.btnUpVersion.setText(QCoreApplication.translate("Assembler", u"+", None))
        self.btnPublish.setText(QCoreApplication.translate("Assembler", u"Publish Current Version", None))
        self.btnReload.setText(QCoreApplication.translate("Assembler", u"Reload Pages", None))
        self.chbSelected.setText(QCoreApplication.translate("Assembler", u"SEL", None))
        self.btnSendPublished.setText(QCoreApplication.translate("Assembler", u"Send Published Versions", None))
        self.linPDFVersion.setText(QCoreApplication.translate("Assembler", u"01", None))
        self.btnGeneratePDF.setText(QCoreApplication.translate("Assembler", u"Generate PDF file", None))
        self.grp_images.setTitle(QCoreApplication.translate("Assembler", u"Page Prewiew", None))
        self.labPage.setText("")
        self.menuHelp.setTitle(QCoreApplication.translate("Assembler", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Assembler", u"Edit", None))
    # retranslateUi

