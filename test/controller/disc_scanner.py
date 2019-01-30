import unittest
import os
from app.controller import disc_scanner


def test_build_file_tree():
    returned = [(node.name, node.level) for node in
                disc_scanner.build_file_tree(os.path.abspath(os.path.join('..', 'test_dir')))]
    expected = [('test_dir/', 0), ('testfile', 1), ('test_subdir/', 1), ('testsubfile', 2)]
    assert returned == expected, \
        'test_build_file_tree failed' \
        'expected: {}' \
        'returned: {}'.format(expected, returned)


def test_get_n_biggest():
    print()
    root = os.path.abspath(os.path.join('..', 'test_dir'))
    expected = [('testfile', 0, root),
                ('testsubfile', 0, os.path.join(root, 'test_subdir')), ]
    returned = [(f.name, f.size, f.pardir) for f in disc_scanner.get_n_biggest(root)]

    assert len(returned) == len(expected), \
        'test_build_file_tree failed' \
        'expected len: {}' \
        'returned len: {}'.format(len(expected), len(returned))

    assert returned == expected, \
        'test_build_file_tree failed' \
        'expected: {}' \
        'returned: {}'.format(expected, returned)


def test_get_n_biggest_directories_only():
    root = os.path.abspath(os.path.join('..', 'test_dir'))
    expected = [('test_subdir', 0, root)]
    returned = [(f.name, f.size, f.pardir) for f in
                disc_scanner.get_n_biggest(root, consider_files=False,
                                           consider_directories=True)]

    assert len(returned) == len(expected), \
        'test_build_file_tree failed' \
        'expected len: {}' \
        'returned len: {}'.format(len(expected), len(returned))

    assert returned == expected, \
        'test_build_file_tree failed' \
        'expected: {}' \
        'returned: {}'.format(expected, returned)


def test_get_n_biggest_all():
    root = os.path.abspath(os.path.join('..', 'test_dir'))
    expected = [('test_subdir', 0, root),
                ('testfile', 0, root),
                ('testsubfile', 0, os.path.join(root, 'test_subdir')), ]
    returned = disc_scanner.get_n_biggest(root, consider_directories=True)

    assert len(returned) == len(expected), \
        'test_build_file_tree failed' \
        'expected len: {}' \
        'returned len: {}'.format(len(expected), len(returned))

    assert returned == expected, \
        'test_build_file_tree failed' \
        'expected: {}' \
        'returned: {}'.format(expected, returned)


if __name__ == '__main__':
    unittest.main()
