from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget


class ResultsDefaultSearchWidget(QWidget):
    """
    Widget class with search results view (grouped by top size used files and directories).
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_default_search_component.ui
        """
        super(ResultsDefaultSearchWidget, self).__init__(parent)
        uic.loadUi('ui/results_default_search_component.ui', self)

        top_size_files_header = ['File', 'Location', 'Size']
        top_size_dirs_header = ['Directory', 'Location', 'Size']

        mock_data_files = [
            ['plik1.txt', 'D:folder\\ukryte', 142],
            ['plik2.txt', 'D:folder\\ukryte\\A', 1420]
        ]

        mock_data_dirs = [
            ['STUDIA', 'D:folder\\nauka', 3256],
            ['python', 'D:folder\\nauka\\projekty', 1233]
        ]

        self.initialize_results_tree()
        self.initialize_top_ten_size_files(top_size_files_header, mock_data_files)
        self.initialize_top_ten_size_dirs(top_size_dirs_header, mock_data_dirs)

    def initialize_results_tree(self):
        """
        Initialize results tree view.
        """
        # https://stackoverflow.com/questions/47102920/pyqt5-how-to-generate-a-qtreeview-from-a-list-of-dictionary-items
        pass

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

        for items in data:
            row = []
            for item in items:
                item = QStandardItem(str(item))
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

        for items in data:
            row = []
            for item in items:
                item = QStandardItem(str(item))
                item.setEditable(False)
                row.append(item)
            model.appendRow(row)

        self.topTenFilesTableView.sortByColumn(2, Qt.DescendingOrder)
        self.topTenFilesTableView.verticalHeader().setVisible(False)
