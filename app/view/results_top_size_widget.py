from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsTopSizeUsedWidget(QWidget):
    """
    Widget class with search results view (grouped by top size used files and directories).
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_top_size_component.ui
        """
        super(ResultsTopSizeUsedWidget, self).__init__(parent)
        uic.loadUi('ui/results_top_size_component.ui', self)
