from threading import Thread

from PyQt5.QtCore import pyqtSignal, QThread

from controller.disc_scanner import build_file_tree, get_n_biggest


class DefaultSearchThread(QThread):
    """"
    Class for apply non blocking search call by given properties
    """
    sig1 = pyqtSignal(dict)

    def __init__(self, parent=None, path=None, n=10):
        """
        Init method.
        :param parent: parent component view
        :param path: path to scan
        :param n: number of n biggest files to find
        """
        QThread.__init__(self)
        self.parent = parent
        self.path = path
        self.n = n
        self.output = {}

    def on_event(self):
        """"
        Listener method.
        """
        Thread(target=self.handle_searching).start()

    def handle_searching(self):
        self.output['tree'] = build_file_tree(self.path)
        self.output['top_n_files'] = get_n_biggest(n=self.n)
        self.output['top_n_dirs'] = get_n_biggest(n=self.n, consider_files=False, consider_directories=True)
        self.sig1.emit(self.output)
