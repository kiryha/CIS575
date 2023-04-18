"""
Book Assembler main module
"""


import os
import glob
import webbrowser
from shutil import copyfile
from PySide2 import QtCore, QtGui, QtWidgets

from ui import ui_assembler_main

from modules.database import init
from modules.database import database
from modules.settings import settings
from modules.pdf import pdf

assembler_root = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


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

        # Data
        self.settings = None
        self.sql_file_path = None
        self.project_root = None
        self.versioned_pages = None
        self.final_pages = None
        self.pdf_files = None
        self.book = None
        self.book_model = None
        self.current_version = None  # UI [ +/- ] counter for selected page

        # Populate data
        self.init_ui()

        # Setup UI calls
        self.actionDocumentation.triggered.connect(self.help)
        self.tabPages.clicked.connect(self.show_page)
        self.btnSetProject.clicked.connect(self.set_project)

        self.btnUpVersion.clicked.connect(lambda: self.show_page(1))
        self.btnDownVersion.clicked.connect(lambda: self.show_page(-1))
        self.btnPublish.clicked.connect(self.publish_page)
        self.btnReload.clicked.connect(self.init_ui)
        self.btnSendPublished.clicked.connect(self.send_published)
        self.btnGeneratePDF.clicked.connect(self.generate_pdf)

    # UI setup
    def set_project(self):
        """
        Select root folder for current project
        """

        project_root = QtWidgets.QFileDialog.getExistingDirectory(self, 'Set Project', self.project_root)

        # Save new settings and update UI
        if project_root:
            project_root = project_root.replace('\\', '/')

            self.settings.set_project_root(project_root)

            self.init_ui()

    def apply_settings(self):

        self.sql_file_path = self.settings.get_sql_file_path()
        self.project_root = self.settings.get_project_root()
        self.versioned_pages = self.settings.get_versioned_pages()
        self.final_pages = self.settings.get_final_pages()
        self.pdf_files = self.settings.get_pdf_files()

    def init_ui(self):
        """
        Read data from database, read files from disc, output data to UI
        """

        # Setup pages table
        self.tabPages.verticalHeader().hide()
        self.tabPages.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabPages.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabPages.horizontalHeader().setStretchLastSection(True)
        self.tabPages.setItemDelegate(AlignDelegate())

        # Load data
        self.settings = settings.Settings(assembler_root)
        self.apply_settings()
        self.linCurrentProject.setText(self.project_root)

        # Init database
        if not os.path.exists(self.sql_file_path):
            init.build_database(self.sql_file_path)

        # Get pages and display in UI
        page_files = glob.glob(f'{self.settings.get_versioned_pages()}/*.jpg')
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

        jpg_path = '{0}/{1}_{2}.jpg'.format(self.versioned_pages, page_number, version)

        if not os.path.exists(jpg_path):
            return

        return jpg_path

    def copy_file_locally(self, page, published_version):
        """
        Copy versioned files to "to_layout" folder without version
        """

        file_path_src = '{0}/{1}_{2}.jpg'.format(self.versioned_pages, page.page_number, published_version)
        file_path_out = '{0}/{1}.jpg'.format(self.final_pages, page.page_number)

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

        self.statusbar.showMessage('Copy complete!')

    def generate_pdf(self):
        """
        Build PDF file fro all pages
        """

        self.statusbar.showMessage('Building PDF file...')

        # Create a folder for PDF files:
        if not os.path.exists(self.pdf_files):
            os.makedirs(self.pdf_files)

        # Build pdf
        path_pdf = '{0}/workbook_{1}.pdf'.format(self.pdf_files, self.linPDFVersion.text())
        print(path_pdf)
        pdf.generate_pdf(self.book, path_pdf, self.versioned_pages)

        self.statusbar.showMessage('PDF file saved at {}'.format(path_pdf))


if __name__ == "__main__":

    # Launch the Book Assembler application
    app = QtWidgets.QApplication([])
    ketamine = Assembler()
    ketamine.show()
    app.exec_()
