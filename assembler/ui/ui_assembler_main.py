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
        Assembler.resize(925, 892)
        self.actionDocumentation = QAction(Assembler)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSettings = QAction(Assembler)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(Assembler)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_8 = QSplitter(self.centralwidget)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.groupBox_2 = QGroupBox(self.splitter_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 90))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnCreateNewProject = QPushButton(self.groupBox_2)
        self.btnCreateNewProject.setObjectName(u"btnCreateNewProject")
        self.btnCreateNewProject.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.btnCreateNewProject)

        self.splitter_3 = QSplitter(self.groupBox_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.splitter_3.addWidget(self.label_2)
        self.comProjects = QComboBox(self.splitter_3)
        self.comProjects.setObjectName(u"comProjects")
        self.splitter_3.addWidget(self.comProjects)

        self.verticalLayout_4.addWidget(self.splitter_3)

        self.splitter_8.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabPages = QTableView(self.groupBox_3)
        self.tabPages.setObjectName(u"tabPages")

        self.verticalLayout_5.addWidget(self.tabPages)

        self.splitter_9 = QSplitter(self.groupBox_3)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.btnDownVersion = QPushButton(self.splitter_9)
        self.btnDownVersion.setObjectName(u"btnDownVersion")
        self.splitter_9.addWidget(self.btnDownVersion)
        self.btnUpVersion = QPushButton(self.splitter_9)
        self.btnUpVersion.setObjectName(u"btnUpVersion")
        self.splitter_9.addWidget(self.btnUpVersion)

        self.verticalLayout_5.addWidget(self.splitter_9)

        self.btnPublish = QPushButton(self.groupBox_3)
        self.btnPublish.setObjectName(u"btnPublish")

        self.verticalLayout_5.addWidget(self.btnPublish)

        self.btnReload = QPushButton(self.groupBox_3)
        self.btnReload.setObjectName(u"btnReload")

        self.verticalLayout_5.addWidget(self.btnReload)

        self.splitter_10 = QSplitter(self.groupBox_3)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.chbSelected = QCheckBox(self.splitter_10)
        self.chbSelected.setObjectName(u"chbSelected")
        self.chbSelected.setMaximumSize(QSize(40, 16777215))
        self.chbSelected.setChecked(True)
        self.splitter_10.addWidget(self.chbSelected)
        self.btnSendPublished = QPushButton(self.splitter_10)
        self.btnSendPublished.setObjectName(u"btnSendPublished")
        self.splitter_10.addWidget(self.btnSendPublished)

        self.verticalLayout_5.addWidget(self.splitter_10)

        self.splitter_11 = QSplitter(self.groupBox_3)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Horizontal)
        self.linPDFVersion = QLineEdit(self.splitter_11)
        self.linPDFVersion.setObjectName(u"linPDFVersion")
        self.linPDFVersion.setMaximumSize(QSize(40, 16777215))
        self.linPDFVersion.setAlignment(Qt.AlignCenter)
        self.splitter_11.addWidget(self.linPDFVersion)
        self.btnGeneratePDF = QPushButton(self.splitter_11)
        self.btnGeneratePDF.setObjectName(u"btnGeneratePDF")
        self.splitter_11.addWidget(self.btnGeneratePDF)

        self.verticalLayout_5.addWidget(self.splitter_11)

        self.splitter_8.addWidget(self.groupBox_3)

        self.horizontalLayout.addWidget(self.splitter_8)

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
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("Assembler", u"Project", None))
        self.btnCreateNewProject.setText(QCoreApplication.translate("Assembler", u"Create New Project", None))
        self.label_2.setText(QCoreApplication.translate("Assembler", u"Current Project", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Assembler", u"Pages", None))
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

