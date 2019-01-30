from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

from controller.disc_scanner import import_data


class ResultsDefaultSearchWidget(QWidget):
    """
    Widget class with search results view (grouped by top size used files and directories).
    """

    def __init__(self, file_tree, top_n_dirs, top_n_files, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_default_search_component.ui
        """
        super(ResultsDefaultSearchWidget, self).__init__(parent)
        uic.loadUi('ui/results_default_search_component.ui', self)

        top_size_files_header = ['File', 'Location', 'Size']
        top_size_dirs_header = ['Directory', 'Location', 'Size']

        self.handle_buttons(parent)
        self.initialize_results_tree(file_tree=file_tree)
        self.initialize_top_ten_size_files(top_size_files_header, data=top_n_files)
        self.initialize_top_ten_size_dirs(top_size_dirs_header, data=top_n_dirs)

    def handle_buttons(self, parent):
        """
        Handle all buttons action events.
        :param parent: - parent window
        """
        self.homeButton.clicked.connect(parent.start_scan_view)

    def initialize_results_tree(self, file_tree):
        """
        Initialize results tree view.
        """
        # https://stackoverflow.com/questions/47102920/pyqt5-how-to-generate-a-qtreeview-from-a-list-of-dictionary-items
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([''])
        self.treeView.header().setDefaultSectionSize(180)
        self.treeView.setModel(model)
        import_data(model, file_tree)

    def initialize_top_ten_size_dirs(self, header_labels, data):
        """
        Initialize top ten size dirs view.
        :param header_labels: labels for table on view
        :param data: data for table on view
        """
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        self.topTenDirsTableView.setModel(model)

        header = self.topTenDirsTableView.horizontalHeader()
        table_width = header.size().width()
        columns_width = [table_width / 9 * 2, table_width / 9 * 5, table_width / 9 * 2]
        for idx, value in enumerate(columns_width):
            self.topTenDirsTableView.setColumnWidth(idx, value)

        for file in data:
            row = []
            item = QStandardItem(str(file.name))
            item.setEditable(False)
            row.append(item)
            item = QStandardItem(str(file.pardir))
            item.setEditable(False)
            row.append(item)
            item = QStandardItem(str(file.size))
            item.setEditable(False)
            row.append(item)
            model.appendRow(row)

        self.topTenDirsTableView.sortByColumn(2, Qt.DescendingOrder)
        self.topTenDirsTableView.verticalHeader().setVisible(False)

    def initialize_top_ten_size_files(self, header_labels, data):
        """
        Initialize top ten size files view.
        :param header_labels: labels for table on view
        :param data: data for table on view
        """
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        self.topTenFilesTableView.setModel(model)

        header = self.topTenFilesTableView.horizontalHeader()
        table_width = header.size().width()
        columns_width = [table_width / 9 * 2, table_width / 9 * 5, table_width / 9 * 2]
        for idx, value in enumerate(columns_width):
            self.topTenFilesTableView.setColumnWidth(idx, value)

        for file in data:
            row = []
            item = QStandardItem(str(file.name))
            item.setEditable(False)
            row.append(item)
            item = QStandardItem(str(file.pardir))
            item.setEditable(False)
            row.append(item)
            item = QStandardItem(str(file.size))
            item.setEditable(False)
            row.append(item)
            model.appendRow(row)

        self.topTenFilesTableView.sortByColumn(2, Qt.DescendingOrder)
        self.topTenFilesTableView.verticalHeader().setVisible(False)
