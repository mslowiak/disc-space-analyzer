from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AdvancedSearchWidget(QWidget):
    def __init__(self, parent=None):
        super(AdvancedSearchWidget, self).__init__(parent)
        uic.loadUi('ui/advanced_search_component.ui', self)
