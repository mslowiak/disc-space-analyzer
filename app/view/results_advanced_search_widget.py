from collections import defaultdict

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

from view.extensions_plot import PlotCanvas


class ResultsAdvancedSearchWidget(QWidget):
    """
    Widget class with advanced search results view (extensions and top size files view).
    """

    def __init__(self, search_results_data, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_advanced_search_component.ui
        """
        super(ResultsAdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/results_advanced_search_component.ui', self)

        pie_chart_labels, pie_chart_values = self.get_data_for_pie_chart(search_results_data)

        top_size_headers = ['File Name', 'Location', 'Extension', 'File Size (KB)']
        top_size_data = self.get_data_for_top_size_list(search_results_data)

        self.handle_buttons(parent)
        self.initialize_top_file_extensions_view(pie_chart_labels, pie_chart_values)
        self.initialize_top_size_files_view(top_size_headers, top_size_data)

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
        table_width = header.size().width()
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

        self.topSizeFilesTableView.verticalHeader().setVisible(False)

    def get_data_for_pie_chart(self, search_results):
        """"
        Responsible for mapping results to compatible format for pie chart view.
        :param search_results: results from advanced search view
        """
        my_ext = list(map(lambda file: file.extension, search_results))
        occurences = defaultdict(int)
        for ext in my_ext:
            occurences[ext] += 1
        return list(occurences.keys()), list(occurences.values())

    def get_data_for_top_size_list(self, search_results):
        """"
        Responsible for mapping results to compatible format for top size list view.
        :param search_results: results from advanced search view
        """
        without_date = list(
            map(lambda file: [file.name, file.location, file.extension, file.file_size], search_results))
        return sorted(without_date, key=lambda x: x[3], reverse=True)
