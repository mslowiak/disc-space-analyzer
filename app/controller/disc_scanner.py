import glob
import os
from collections import namedtuple, deque

from PyQt5.QtGui import QStandardItem

from model.file_tree import Node

File = namedtuple('File', ['name', 'size', 'pardir'])


def build_file_tree(start_path=os.path.expanduser('~')):
    root = Node(start_path, os.path.isdir(start_path), level=0, parent=None)
    queue = [root]
    ret = []
    while queue:
        try:
            node = queue.pop(0)
            ret.append(node)
            if node.is_dir:
                node.children = [Node(os.path.abspath(os.path.join(node.path, path)),
                                      os.path.isdir(os.path.abspath(os.path.join(node.path, path))), level=node.level + 1, parent=node)
                                 for path in os.listdir(node.path)]
                queue.extend(node.children)
        except (PermissionError, FileNotFoundError):
            continue
    return ret


def update_biggest(n, biggest, files, root):
    for f in files:
        f = os.path.abspath(os.path.join(root, f))
        f_size = os.path.getsize(f)
        biggest.append(File(f, f_size, os.path.abspath(os.path.join(f, os.pardir))))
        if len(biggest) > n:
            min_ = min(biggest, key=lambda p: p.size)
            biggest.remove(min_)
    return biggest


def get_n_biggest(start_dir=os.path.expanduser('~'), n=10, consider_files=True, consider_directories=False,
                  recursive=True):
    biggest = []
    if recursive:
        for root, dirs, files in os.walk(os.path.abspath(start_dir)):
            try:
                if consider_directories:
                    biggest = update_biggest(n, biggest, dirs, root)
                if consider_files:
                    biggest = update_biggest(n, biggest, files, root)
            except (FileNotFoundError, OSError):
                continue
    else:
        biggest = [File(f, os.path.getsize(f), os.path.abspath(os.path.join(f, os.pardir))) for f in
                   os.listdir(os.path.abspath(start_dir))]
        if not consider_directories:
            biggest = [f for f in biggest if not os.path.isdir(os.path.abspath(os.path.join(start_dir, f.name)))]
        if not consider_files:
            biggest = [f for f in biggest if os.path.isdir(os.path.abspath(os.path.join(start_dir, f.name)))]
    return sorted(biggest, key=lambda p: p.size, reverse=True)[:n]


def advanced_search(path=None, size_range=None, date_range=None, extensions=None):
    if not path:
        path = os.path.expanduser('~')
    if extensions:
        files = []
        for extension in extensions:
            files.extend(glob.glob(os.path.join(path, '**', f'*.{extension}'), recursive=True))
    else:
        files = [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]
    if date_range:
        files = [file for file in files if date_range[0] <= os.path.getmtime(file) < date_range[1]]
    if size_range:
        files = [file for file in files if size_range[0] <= os.path.getsize(file) < size_range[1]]
    return [os.path.abspath(file) for file in files]


def import_data(model, file_tree, root=None):
    model.setRowCount(0)
    if root is None:
        root = model.invisibleRootItem()
    seen = {}
    queue = deque(file_tree)
    while queue:
        node = queue.popleft()
        if node.level == 0:
            parent = root
        else:
            parent_node_name = node.parent.name
            if parent_node_name not in seen:
                queue.append(node)
                continue
            parent = seen[parent_node_name]
        node_name = node.name
        parent.appendRow([
            QStandardItem(node_name)
        ])
        seen[node_name] = parent.child(parent.rowCount() - 1)


if __name__ == '__main__':
    search_results = advanced_search(path=os.path.join('..', '..', '..', '..'),
                                     size_range=(0, 1000000000000000000000000000))
    print(search_results)
    print(len(search_results))
    search_results = advanced_search(path=os.path.join('..', '..', '..', '..'))
    print(search_results)
    print(len(search_results))
    # print(get_n_biggest('..', n=3, recursive=False, consider_directories=True))
    # tree = build_file_tree(os.path.abspath('.'))
    # tree.bfs()
