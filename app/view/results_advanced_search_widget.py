from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

from view.extensions_plot import PlotCanvas


class ResultsAdvancedSearchWidget(QWidget):
    """
    Widget class with advanced search results view (extensions and top size files view).
    """

    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_advanced_search_component.ui
        """
        super(ResultsAdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/results_advanced_search_component.ui', self)

        mock_labels = ['.exe', '.zip', '.doc', '.txt']
        mock_percentage = [15, 30, 45, 10]

        mock_headers = ['File Name', 'Location', 'Extension', 'File Size (KB)']
        mock_data = [
            ['plik1.txt', 'D:folder\\ukryte', 'txt', 142],
            ['plik1.txt', 'D:folder\\ukryte', 'txt', 142]
        ]

        self.handle_buttons(parent)
        self.initialize_top_file_extensions_view(mock_labels, mock_percentage)
        self.initialize_top_size_files_view(mock_headers, mock_data)

    def handle_buttons(self, parent):
        """
        Handle all buttons action events.
        :param parent: - parent window
        """
        self.homeButton.clicked.connect(parent.start_scan_view)

    def initialize_top_file_extensions_view(self, labels, values):
        """
        Initialize view with grouped search results by extensions as a pie chart.
        :param labels: available extensions
        :param values: percentage size of given extensions
        """
        pie_chart = PlotCanvas(labels=labels, percentage=values, parent=self.topFileExtensionsPieChart)
        pie_chart.move(1, 1)

    def initialize_top_size_files_view(self, header_labels, data):
        """"
        Initialize view with search results ordered by size.
        :param header_labels: header labels for table
        :param data: table data to be inserted to the table
        """

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(header_labels)

        self.topSizeFilesTableView.setModel(model)

        header = self.topSizeFilesTableView.horizontalHeader()
        table_width = header.size().width() - 15
        columns_width = [table_width / 12 * 3, table_width / 12 * 5, table_width / 12 * 2, table_width / 12 * 2]
        for idx, value in enumerate(columns_width):
            self.topSizeFilesTableView.setColumnWidth(idx, value)

        for items in data:
            row = []
            for item in items:
                item = QStandardItem(str(item))
                item.setEditable(False)
                row.append(item)
            model.appendRow(row)

        self.topSizeFilesTableView.sortByColumn(0, Qt.AscendingOrder)
