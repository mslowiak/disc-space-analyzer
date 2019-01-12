from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResultsExtensionsWidget(QWidget):
    """
    Widget class with search results view (grouped by extensions).
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/results_extensions_component.ui
        """
        super(ResultsExtensionsWidget, self).__init__(parent)
        uic.loadUi('ui/results_extensions_component.ui', self)
