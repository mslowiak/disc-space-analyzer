from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel

from controller.default_search_async import DefaultSearchThread


class ScanWidget(QWidget):
    """
    Widget class with scan view.
    """

    sig = pyqtSignal(str)

    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/scan_component.ui
        """
        super(ScanWidget, self).__init__(parent)
        uic.loadUi('ui/scan_component.ui', self)
        self.parent = parent
        self.search_thread = DefaultSearchThread()
        self.handle_buttons(parent)

    def handle_buttons(self, parent):
        """
        Method handling buttons on click action
        """
        self.advancedScanButton.clicked.connect(parent.start_advanced_search_view)
        self.fastScanButton.clicked.connect(self.handle_default_scan_click)

    def handle_default_scan_click(self):
        """
        Handle scan button action event.
        Responsible for enabling waiting bar
        """
        label = QLabel(self)
        label.setText("SEARCHING")
        self.setDisabled(True)

        label_width = 500
        label_height = 100
        label_x_pos = self.size().width() // 2 - label_width // 2
        label_y_pos = self.size().height() // 2 - label_height // 2

        movie = QMovie("ajax-loader.gif")
        label.setGeometry(label_x_pos, label_y_pos, label_width, label_height)
        label.setFrameStyle(Qt.FramelessWindowHint)
        label.setMovie(movie)
        label.show()
        movie.setScaledSize(label.size())
        movie.start()

        self.sig.connect(self.search_thread.on_event)
        self.sig.emit("search")
        self.search_thread.start()
        self.search_thread.sig1.connect(self.handle_processed_paths)

    def handle_processed_paths(self, search_results_data):
        """
        Handle search results.
        Responsible for changing view to results view
        """
        self.search_thread.exit(1)
        self.parent.start_results_default_search_view(search_results_data)
