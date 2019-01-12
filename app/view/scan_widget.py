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

        # the way to create an action on button click
        # self.pushButton.clicked.connect(parent.start_scan_view)
