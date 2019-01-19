from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ScanWidget(QWidget):
    """
    Widget class with scan view.
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/scan_component.ui
        """
        super(ScanWidget, self).__init__(parent)
        uic.loadUi('ui/scan_component.ui', self)
        self.handle_buttons(parent)

    def handle_buttons(self, parent):
        """
        Method handling buttons on click action
        """
        self.advancedScanButton.clicked.connect(parent.start_advanced_search_view)
        self.fastScanButton.clicked.connect(parent.start_results_default_search_view)
