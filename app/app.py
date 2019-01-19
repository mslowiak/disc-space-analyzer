import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from view.results_advanced_search_widget import ResultsAdvancedSearchWidget
from view.scan_widget import ScanWidget
from view.advanced_search_widget import AdvancedSearchWidget
from view.results_rarely_used_widget import ResultsRarelyUsedWidget
from view.results_top_size_widget import ResultsTopSizeUsedWidget


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

    def start_results_advanced_search(self):
        """
        Displays widget in main window.
        Contains results with top size files grouped by extensions.
        """
        self.hide_widget()
        self.actual_widget = ResultsAdvancedSearchWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results of advanced search")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_rarely_used_view(self):
        """
        Displays widget in main window.
        Contains results with rarely used files.
        """
        self.hide_widget()
        self.actual_widget = ResultsRarelyUsedWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results rarely used files")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_top_size_view(self):
        """
        Displays widget in main window.
        Contains results with top size files and directories.
        """
        self.hide_widget()
        self.actual_widget = ResultsTopSizeUsedWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results top size files and dirs")
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
