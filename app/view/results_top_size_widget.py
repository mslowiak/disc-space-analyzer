from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsTopSizeUsedWidget(QWidget):
    def __init__(self, parent=None):
        super(ResultsTopSizeUsedWidget, self).__init__(parent)
        uic.loadUi('ui/results_top_size_component.ui', self)
