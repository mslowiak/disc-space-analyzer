import unittest
import os
from app.controller import disc_scanner


def test_build_file_tree():
    returned = [(node.name, node.level) for node in disc_scanner.build_file_tree(os.path.abspath(os.path.join('..', 'test_dir')))]
    # returned = tree.bfs()
    expected = {1: ['test_dir/'], 2: ['testfile', 'test_subdir/'], 3: ['testsubfile']}
    print(returned)
    # assert returned == expected, \
    #     'test_build_file_tree failed' \
    #     'expected: {}' \
    #     'returned: {}'.format(expected, returned)


def test_get_n_biggest():
    print()
    n_biggest = disc_scanner.get_n_biggest(os.path.join('..', 'test_dir'))
    print(len(n_biggest))
    print(n_biggest)


def test_get_n_biggest_directories_only():
    print()
    n_biggest = disc_scanner.get_n_biggest(os.path.join('..', 'test_dir'), consider_files=False,
                                           consider_directories=True)
    print(len(n_biggest))
    print(n_biggest)


def test_get_n_biggest_all():
    print()
    n_biggest = disc_scanner.get_n_biggest(os.path.expanduser('~'), consider_directories=True)
    print(len(n_biggest))
    print(n_biggest)


if __name__ == '__main__':
    unittest.main()
