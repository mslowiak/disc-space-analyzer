import glob
import os
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QThread


class AdvancedSearchThread(QThread):
    sig1 = pyqtSignal(list)

    def __init__(self, parent=None, path=None, size_range=None, date_range=None, extensions=None):
        QThread.__init__(self)
        self.parent = parent
        self.path = path
        self.size_range = size_range
        self.date_range = date_range
        self.extensions = extensions
        self.paths = [1, 2]

    def on_event(self):
        Thread(target=self.handle_searching).start()

    def handle_searching(self):
        if not self.path:
            self.path = os.path.expanduser('~')
        if self.extensions:
            files = []
            for extension in self.extensions:
                files.extend(glob.glob(os.path.join(self.path, '**', f'*.{extension}'), recursive=True))
        else:
            files = [os.path.join(root, file) for root, dirs, files in os.walk(self.path) for file in files]
        if self.date_range:
            files = [file for file in files if self.date_range[0] <= os.path.getmtime(file) < self.date_range[1]]
        if self.size_range:
            files = [file for file in files if self.size_range[0] <= os.path.getsize(file) < self.size_range[1]]
        self.paths = [os.path.abspath(file) for file in files]
        self.sig1.emit(self.paths)
