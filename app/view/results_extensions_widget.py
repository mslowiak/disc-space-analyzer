from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from view.extensions_plot import PlotCanvas


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

        mock_labels = ['.exe', '.zip', '.doc', '.txt']
        mock_percentage = [15, 30, 45, 10]

        PlotCanvas(labels=mock_labels, percentage=mock_percentage, parent=self.graph)

        self.handle_buttons(parent)

    def handle_buttons(self, parent):
        """
        Handle all buttons action events.
        :param parent: - parent window
        """
        self.homeButton.clicked.connect(parent.start_scan_view)
