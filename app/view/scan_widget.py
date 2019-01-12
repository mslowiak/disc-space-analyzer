from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


def temporary_method(name):
    print("Handle " + name)


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
        self.fastScanButton.clicked.connect(lambda: temporary_method("fastScanButton"))
