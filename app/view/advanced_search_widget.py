from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AdvancedSearchWidget(QWidget):
    """
    Widget class with advanced search view.
    """
    def __init__(self, parent=None):
        """"
        Init method.
        Loads view defined in ui/advanced_search_component.ui
        """
        super(AdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/advanced_search_component.ui', self)
