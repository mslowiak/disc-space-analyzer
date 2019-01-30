import glob
import os
import time
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QThread

from model.file_tree import File
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

    def to_file(self, file_info_tuple):
        """"
        Mapper - properties to File class object
        :param file_info_tuple: tuple with path and stats
        """
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
