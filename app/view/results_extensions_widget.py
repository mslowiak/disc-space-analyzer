from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsExtensionsWidget(QWidget):
    def __init__(self, parent=None):
        super(ResultsExtensionsWidget, self).__init__(parent)
        uic.loadUi('ui/results_extensions_component.ui', self)
