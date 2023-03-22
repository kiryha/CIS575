"""
Book Assembler main module
"""


import os
import glob
import webbrowser
from shutil import copyfile
from PySide2 import QtCore, QtGui, QtWidgets

from ui import ui_assembler_main
from ui import ui_assembler_settings

from modules.database import init
from modules.database import database
from modules.settings import settings
from modules.pdf import pdf

assembler_root = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


class SettingsUI(QtWidgets.QDialog, ui_assembler_settings.Ui_Settings):
    """
    Class to edit Book Assembler settings by user
    """

    def __init__(self, parent=None):
        # SETUP UI WINDOW
        super(SettingsUI, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent

        # UI functionality
        self.btnSaveSettings.clicked.connect(self.update_settings)
        self.btnSaveSettings.clicked.connect(self.close)

    def showEvent(self, event):
        """
        Read settings from settings.json and fill UI
        """

        self.linProjectFolder.setText(settings_data.project_root)
        self.linVersionedPages.setText(settings_data.versioned_pages)
        self.linFinalPages.setText(settings_data.final_pages)
        self.linPDFfiles.setText(settings_data.pdf_files)
        self.linSQLfile.setText(settings_data.sql_file_path)

    def update_settings(self):
        """
        Save edited strings to settings.json
        """

        self.parent.update_settings(self.linProjectFolder.text(),
                                    self.linVersionedPages.text(),
                                    self.linFinalPages.text(),
                                    self.linPDFfiles.text(),
                                    self.linSQLfile.text())


class AlignDelegate(QtWidgets.QItemDelegate):
    """
    Center alignment for data model of the pages table
    """

    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QtWidgets.QItemDelegate.paint(self, painter, option, index)


class BookModel(QtCore.QAbstractTableModel):
    """
    PySide data model for a book
    """

    def __init__(self, book, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.book = book
        self.header = ['  Number  ', '  Pub ', '  Sent ', '  Description  ']

    # Build-in functions
    def flags(self, index):
        """
        Define table behaviour
        """

        column = index.column()
        if column == 3:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        """
        Set name for table columns
        """

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]

    def rowCount(self, parent):
        """
        Calculate row count
        """

        if not self.book.list_pages:
            return 0

        return len(self.book.list_pages)

    def columnCount(self, parent):
        """
        Define column count for table
        """

        return 4

    def data(self, index, role):
        """
        Display data from database in UI
        """

        if not index.isValid():
            return

        row = index.row()
        column = index.column()
        page = self.book.list_pages[row]

        # Paint text red if published version != uploaded version
        if role == QtCore.Qt.ForegroundRole:
            if column == 2:
                if page.get_published_version() != page.get_sent_version():
                    return QtGui.QBrush(QtGui.QColor('#c90404'))

        # Get page object
        if role == QtCore.Qt.UserRole + 1:
            return page

        # Display page data
        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return page.page_number

            if column == 1:
                return page.get_published_version()

            if column == 2:
                return page.get_sent_version()

            if column == 3:
                return page.description

        # Edit description
        if role == QtCore.Qt.EditRole:
            if column == 3:
                return page.description

    def setData(self, index, cell_data, role=QtCore.Qt.EditRole):
        """
        When "Description" table cell is edited
        """

        row = index.row()
        column = index.column()
        page = self.book.list_pages[row]

        if role == QtCore.Qt.EditRole:

            if column == 3:
                page.description = cell_data
                page.update_page()
                self.book.update_page(page)

            return True


class Assembler(QtWidgets.QMainWindow, ui_assembler_main.Ui_Assembler):
    """
    Main class of Book Assembler
    """

    def __init__(self, parent=None):
        super(Assembler, self).__init__(parent=parent)

        # SETUP UI
        self.setupUi(self)

        # Setup pages table
        self.tabPages.verticalHeader().hide()
        self.tabPages.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabPages.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabPages.horizontalHeader().setStretchLastSection(True)
        self.tabPages.setItemDelegate(AlignDelegate())

        # Data
        self.book = None
        self.book_model = None
        self.current_version = None  # UI [ +/- ] counter for selected page

        # Populate data
        self.init_ui()

        # Setup UI
        self.actionSettings.triggered.connect(self.edit_settings)
        self.actionDocumentation.triggered.connect(self.help)
        self.tabPages.clicked.connect(self.show_page)

        self.btnUpVersion.clicked.connect(lambda: self.show_page(1))
        self.btnDownVersion.clicked.connect(lambda: self.show_page(-1))
        self.btnPublish.clicked.connect(self.publish_page)
        self.btnReload.clicked.connect(self.init_ui)
        self.btnSendPublished.clicked.connect(self.send_published)
        self.btnGeneratePDF.clicked.connect(self.generate_pdf)

    # UI setup
    def init_ui(self):
        """
        Read data from database, read files from disc, output data to UI
        """

        page_files = glob.glob('{0}/*.jpg'.format(settings_data.versioned_pages))
        self.book = database.Book(page_files)
        self.book.get_pages()

        self.book_model = BookModel(self.book)
        self.tabPages.setModel(self.book_model)

    def help(self):
        """
        Launch help in web browser
        """

        file_help = '{0}/help/html/index.html'.format(assembler_root)
        webbrowser.open(file_help)

    # Functionality
    def get_jpg_path(self, page_number, version):
        """
        Get page file path by page number and version
        :param page_number:
        :param version:
        :return: string path to page file, None if JPG does not exists
        """

        jpg_path = '{0}/{1}_{2}.jpg'.format(settings_data.versioned_pages, page_number, version)

        if not os.path.exists(jpg_path):
            return

        return jpg_path

    def copy_file_locally(self, page, published_version):
        """
        Copy versioned files to "to_layout" folder without version
        """

        file_path_src = '{0}/{1}_{2}.jpg'.format(settings_data.versioned_pages, page.page_number, published_version)
        file_path_out = '{0}/{1}.jpg'.format(settings_data.final_pages, page.page_number)

        copyfile(file_path_src, file_path_out)

        # Check if snapshot of current version exists, create if not
        snapshot = page.get_sent_snapshot_by_version(published_version)
        if not snapshot:
            snapshot = page.add_sent_snapshot(published_version)

        # Record published version to page and update database
        page.sent_id = snapshot.id
        page.update_page()

        # Update pages list with a new page data
        self.book_model.layoutAboutToBeChanged.emit()
        self.book.update_page(page)
        self.book_model.layoutChanged.emit()

        return file_path_out

    def copy_file_to_drive(self, page, file_path_out):
        """
        Upload file to Google Drive
        """

        folder_token = {'q': "'{0}' in parents and trashed=false".format(settings_data.jpeg_folder)}
        existing_pages = self.google_drive.ListFile(folder_token).GetList()

        # Delete existing file
        for existing_page in existing_pages:
            if existing_page['title'] == '{0}.jpg'.format(page.page_number):
                existing_page.Delete()

        # Upload new file
        google_file = self.google_drive.CreateFile({'parents': [{'id': settings_data.jpeg_folder}],
                                               'title': '{0}.jpg'.format(page.page_number)})
        google_file.SetContentFile(file_path_out)
        google_file.Upload()

        print('>> Page {0} uploaded.'.format(page.page_number))

    def get_selected_page_numbers(self):
        """
        Create a string list of selected pages
        """

        selected_pages = []

        indexes = self.tabPages.selectionModel().selectedIndexes()
        for index in indexes:
            page_number = index.data(QtCore.Qt.DisplayRole)
            selected_pages.append(page_number)

        return selected_pages

    def update_settings(self, project_folder, versioned_pages, final_pages, pdf_files, sql_file_path):
        """
        Save settings edited by user to settings.json
        """

        settings.set_settings(project_folder, versioned_pages, final_pages, pdf_files, sql_file_path)

    # UI calls
    def edit_settings(self):
        """
        Launch Edit Setting window
        """

        settings_ui = SettingsUI(self)
        settings_ui.show()

    def show_page(self, shift=None):
        """
        Display image in UI
        Show higher or lover versions with [ + ] or [ - ] buttons
        """

        # Get selected page
        indexes = self.tabPages.selectionModel().selectedIndexes()

        if not indexes:
            self.statusbar.showMessage('WARNING! Please, select page to explore versions!')
            return

        page = indexes[0].data(QtCore.Qt.UserRole + 1)

        # If [ + ] or [ - ] buttons pressed, get next or previous version
        if type(shift) == int:

            if self.current_version:
                version = self.current_version
            else:
                version = page.get_published_version()

                if not version:
                    version = '01'

            int_version = int(version) + shift
            version = '{0:02d}'.format(int_version)
            self.current_version = version

        # If page cell clicked in UI, get published version
        else:
            version = page.get_published_version()

            if not version:
                version = '01'

            self.current_version = None

        # Show JPG
        jpg_path = self.get_jpg_path(page.page_number, version)

        if not jpg_path:
            self.labPage.setPixmap(None)
            self.statusbar.showMessage('Page {0} version {1} does not exists!'.format(page.page_number, version))
            return

        pixmap = QtGui.QPixmap(jpg_path)
        height = self.grp_images.height() - 40  # Get height of groupBox parent widget and scale JPG to fit it
        self.labPage.resize(height/1.295, height)
        self.labPage.setPixmap(pixmap.scaled(self.labPage.size(), QtCore.Qt.IgnoreAspectRatio))

        # Report page number and version shown
        self.statusbar.showMessage('Loaded page {0} version {1}'.format(page.page_number, version))

    def publish_page(self):
        """
        Publish current version for selected page
        """

        # Get selected page
        indexes = self.tabPages.selectionModel().selectedIndexes()

        if not indexes:
            self.statusbar.showMessage('ERROR! Select page to publish!')
            return

        page = indexes[0].data(QtCore.Qt.UserRole + 1)

        # Get current version
        version = self.current_version
        if not version:
            version = '01'

        # Get path to JPG
        jpg_path = self.get_jpg_path(page.page_number, version)
        if not jpg_path:
            self.statusbar.showMessage('ERROR! {} version of {} page does not exists!'.format(version, page.page_number))
            return

        # Check if snapshot of current version exists, create if not
        snapshot = page.get_published_snapshot_by_version(version)
        if not snapshot:
            # snapshot = add_published_snapshot(VersionSnapshot(page.id, version))
            snapshot = page.add_published_snapshot(version)

        # Record published version to page
        page.published_id = snapshot.id
        page.update_page()

        # Update pages list with a new page data
        self.book_model.layoutAboutToBeChanged.emit()
        self.book.update_page(page)
        self.book_model.layoutChanged.emit()

        # Report
        self.statusbar.showMessage('Published {} version of page {}'.format(version, page.page_number))

    def send_published(self):
        """
        Copy files to layout folder and upload to Google Drive
        """

        self.statusbar.showMessage('Copy files to final folder...')

        selected_pages = self.get_selected_page_numbers()

        # Process pages
        for page in self.book.list_pages:

            # Skip unselected pages
            if self.chbSelected.isChecked():
                if page.page_number not in selected_pages:
                    continue

            # Skip published version
            published_version = page.get_published_version()
            if not published_version:
                continue

            # Skip versions without update
            if published_version == page.get_sent_version():
                continue

            # Copy file to local folder
            file_path_out = self.copy_file_locally(page, published_version)

            # Upload file do google drive
            # self.copy_file_to_drive(page, file_path_out)

        self.statusbar.showMessage('Copy complete!')

    def generate_pdf(self):
        """
        Build PDF file fro all pages
        """

        self.statusbar.showMessage('Building PDF file...')

        # Create a folder for PDF files:
        if not os.path.exists(settings_data.pdf_files):
            os.makedirs(settings_data.pdf_files)

        # Build pdf
        path_pdf = '{0}/workbook_{1}.pdf'.format(settings_data.pdf_files, self.linPDFVersion.text())
        pdf.generate_pdf(self.book, path_pdf)

        self.statusbar.showMessage('PDF file saved at {}'.format(path_pdf))


if __name__ == "__main__":

    # Read settings from JSON file
    settings_data = settings.get_settings()

    # Init database
    if not os.path.exists(settings_data.sql_file_path):
        init.build_database(settings_data.sql_file_path)

    # Launch the Book Assembler application
    app = QtWidgets.QApplication([])
    ketamine = Assembler()
    ketamine.show()
    app.exec_()
