import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from view.scan_widget import ScanWidget
from view.advanced_search_widget import AdvancedSearchWidget
from view.results_extensions_widget import ResultsExtensionsWidget
from view.results_rarely_used_widget import ResultsRarelyUsedWidget
from view.results_top_size_widget import ResultsTopSizeUsedWidget


class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent)
        self.setFixedSize(800, 800)
        self.actual_widget = None
        self.start_scan_view()

    def start_scan_view(self):
        self.hide_widget()
        self.actual_widget = ScanWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Scan now")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_advanced_search_view(self):
        self.hide_widget()
        self.actual_widget = AdvancedSearchWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Advanced search")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_extensions_view(self):
        self.hide_widget()
        self.actual_widget = ResultsExtensionsWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results top size file extensions")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_rarely_used_view(self):
        self.hide_widget()
        self.actual_widget = ResultsRarelyUsedWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results rarely used files")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def start_results_top_size_view(self):
        self.hide_widget()
        self.actual_widget = ResultsTopSizeUsedWidget(self)
        self.setWindowTitle("Disc Space Analyzer - Results top size files and dirs")
        self.setCentralWidget(self.actual_widget)
        self.show()

    def hide_widget(self):
        if self.actual_widget:
            self.actual_widget.hide()


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW = AppMainWindow()
    WINDOW.show()
    sys.exit(APP.exec_())
