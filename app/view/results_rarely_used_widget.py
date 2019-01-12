from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsRarelyUsedWidget(QWidget):
    """
    Widget class with search results view (grouped by rarely used files).
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_rarely_used_component.ui
        """
        super(ResultsRarelyUsedWidget, self).__init__(parent)
        uic.loadUi('ui/results_rarely_used_component.ui', self)
