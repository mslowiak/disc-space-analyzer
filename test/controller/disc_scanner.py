import unittest
import os
from app.controller import disc_scanner


def test_build_file_tree():
    tree = disc_scanner.build_file_tree(os.path.abspath(os.path.join('..', 'test_dir')))
    returned = tree.bfs()
    expected = {1: ['test_dir/'], 2: ['testfile', 'test_subdir/'], 3: ['testsubfile']}
    assert returned == expected, \
        'test_build_file_tree failed' \
        'expected: {}' \
        'returned: {}'.format(expected, returned)


def test_get_n_biggest():
    print(disc_scanner.get_n_biggest(os.path.join('..', 'test_dir')))


if __name__ == '__main__':
    unittest.main()
