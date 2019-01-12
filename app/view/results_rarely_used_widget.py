from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsRarelyUsedWidget(QWidget):
    def __init__(self, parent=None):
        super(ResultsRarelyUsedWidget, self).__init__(parent)
        uic.loadUi('ui/results_rarely_used_component.ui', self)
