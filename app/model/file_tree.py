import os


class Node:
    def __init__(self, path, is_dir):
        self.path = path
        self.name = os.path.basename(path)
        self.is_dir = is_dir
        if self.is_dir:
            self.name += '/'
        self.children = []

    def get_children_dirs(self):
        return [child for child in self.children if os.path.isdir(child.path)]


class Tree:
    def __init__(self, root):
        self.root = root

    def bfs(self):
        height = self._height(self.root)
        nodes = {}
        for i in range(1, height + 1):
            nodes[i] = self._bfs(self.root, i)
        return nodes

    def _bfs(self, node, level):
        nodes = []
        if not node:
            return
        if level == 1:
            return [node.name]
        elif level > 1:
            for child in node.children:
                nodes.extend(self._bfs(child, level - 1))
        return nodes

    def height(self):
        self._height(self.root)

    def _height(self, node):
        if not node.is_dir:
            return 1
        heights = []
        for child in node.children:
            heights.append(self._height(child))
        return max(heights) + 1 if heights else 0


class File:
    def __init__(self, name, location, extension, file_size, creation_date):
        self.name = name
        self.location = location
        self.extension = extension
        self.file_size = file_size
        self.creation_date = creation_date
