import glob
import os
import time
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QThread

from model.file_tree import File


class AdvancedSearchThread(QThread):
    sig1 = pyqtSignal(list)

    def __init__(self, parent=None, path=None, size_range=None, date_range=None, extensions=None):
        QThread.__init__(self)
        self.parent = parent
        self.path = path
        self.size_range = size_range
        self.date_range = date_range
        self.extensions = extensions
        self.output = []

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
        tuples = [(os.path.abspath(file), os.stat(os.path.abspath(file))) for file in files]
        self.output = [self.toFile(file_info_tuple) for file_info_tuple in tuples]
        self.sig1.emit(self.output)

    def toFile(self, file_info_tuple):
        f_path = file_info_tuple[0]
        f_stats = file_info_tuple[1]
        split_path = os.path.split(f_path)

        f_dir_to_file = split_path[0]
        split_file = os.path.splitext(split_path[1])
        f_file_name = split_file[0]
        f_file_ext = split_file[1]
        f_file_size = f_stats.st_size
        f_date_time = time.strftime("%D %H:%M", time.localtime(f_stats.st_mtime))

        return File(
            name=f_file_name,
            location=f_dir_to_file,
            extension=f_file_ext,
            file_size=f_file_size,
            creation_date=f_date_time
        )
