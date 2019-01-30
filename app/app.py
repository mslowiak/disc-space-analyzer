import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from view.advanced_search_widget import AdvancedSearchWidget
from view.results_advanced_search_widget import ResultsAdvancedSearchWidget
from view.results_default_search_widget import ResultsDefaultSearchWidget
from view.scan_widget import ScanWidget


class AppMainWindow(QMainWindow):
    """
    Main class of app which manages of view changing.
    """

    def __init__(self, parent=None):
        """
        Init method.
        Sets size of application and calls first view to display.
        """
        super(AppMainWindow, self).__init__(parent)
        self.setFixedSize(1200, 800)
        self.actual_widget = None
        self.start_scan_view()

    def start_scan_view(self):
        """
        Displays widget in main window.
        Contains scan button to start searching files in OS.
        """
        self.hide_widget()
        self.actual_widget = ScanWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Scan now")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_advanced_search_view(self):
        """
        Displays widget in main window.
        Contains advanced search options and scan button to start searching files in OS.
        """
        self.hide_widget()
        self.actual_widget = AdvancedSearchWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Advanced search")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_advanced_search_view(self, search_results_data):
        """
        Displays widget in main window.
        Contains results with from advanced search.
        """
        self.hide_widget()
        self.actual_widget = ResultsAdvancedSearchWidget(search_results_data=search_results_data, parent=self)
        self.setWindowTitle("Disc Space Analyzer - Results of advanced search")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_default_search_view(self, search_data_results_dict):
        """
        Displays widget in main window.
        Contains results from default search.
        """
        self.hide_widget()
        self.actual_widget = ResultsDefaultSearchWidget(file_tree=search_data_results_dict['tree'],
                                                        top_n_dirs=search_data_results_dict['top_n_dirs'],
                                                        top_n_files=search_data_results_dict['top_n_files'],
                                                        parent=self)
        self.setWindowTitle("Disc Space Analyzer - Results of default search")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def hide_widget(self):
        """
        Help method which hide actually visible widget.
        Used when changing between views.
        """
        if self.actual_widget:
            self.actual_widget.hide()


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW = AppMainWindow()
    WINDOW.show()
    sys.exit(APP.exec_())
