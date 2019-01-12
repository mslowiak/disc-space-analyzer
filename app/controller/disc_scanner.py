import os
from model.file_tree import Tree, Node


def build_file_tree(start_path):
    root = Node(start_path, os.path.isdir(start_path))
    tree = Tree(root)
    queue = [root]
    while queue:
        node = queue.pop(0)
        node.children = [Node(os.path.abspath(os.path.join(node.path, path)),
                              os.path.isdir(os.path.abspath(os.path.join(node.path, path))))
                         for path in os.listdir(node.path)]
        queue.extend(node.get_children_dirs())
    return tree


def update_biggest(n, biggest, files, root):
    for f in files:
        f = os.path.abspath(os.path.join(root, f))
        f_size = os.path.getsize(f)
        biggest.append((f, f_size))
        if len(biggest) > n:
            min_ = min(biggest, key=lambda tup: tup[1])
            biggest.remove(min_)
    return biggest


def get_n_biggest(start_dir=os.path.expanduser('~'), n=10, consider_files=True, consider_directories=False, recursive=True):
    biggest = []
    if recursive:
        for root, dirs, files in os.walk(os.path.abspath(start_dir)):
            if consider_directories:
                update_biggest(n, biggest, dirs, root)
            if consider_files:
                update_biggest(n, biggest, files, root)
    else:
        biggest = os.listdir(os.path.abspath(start_dir))
        if not consider_directories:
            biggest = [f for f in biggest if not os.path.isdir(os.path.abspath(os.path.join(start_dir, f)))]
        if not consider_files:
            biggest = [f for f in biggest if os.path.isdir(os.path.abspath(os.path.join(start_dir, f)))]
    return sorted(biggest, key=lambda tup:tup[1], reverse=True)[:n]


if __name__ == '__main__':
    print(get_n_biggest('..', n=3, recursive=False, consider_directories=True))
    # tree = build_file_tree(os.path.abspath('.'))
    # tree.bfs()