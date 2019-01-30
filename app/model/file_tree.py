import os
from collections import namedtuple

File_short = namedtuple('File', ['name', 'size', 'pardir'])


class Node:
    def __init__(self, path, is_dir, level, parent):
        self.path = path
        self.name = os.path.basename(path)
        self.level = level
        self.parent = parent
        self.is_dir = is_dir
        if self.is_dir:
            self.name += '/'
        self.children = []


class File:
    def __init__(self, name, location, extension, file_size, creation_date):
        self.name = name
        self.location = location
        self.extension = extension
        self.file_size = file_size
        self.creation_date = creation_date
