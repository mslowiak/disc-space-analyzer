from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    """
    Wrapper that allows to put matplotlibcode in QT application
    """
    def __init__(self, labels, percentage, parent=None):
        fig = Figure(figsize=(9, 4.5), dpi=100)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(labels, percentage)

    def plot(self, labels, percentage):
        """
        Plots a pie chart with labels and percentage of extensions
        :param labels:
        :param percentage:
        """
        axe = self.figure.add_subplot(111)
        axe.pie(percentage, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        axe.axis('equal')
        self.draw()
