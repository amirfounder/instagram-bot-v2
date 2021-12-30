import os
import shutil
from src.data_manager.files import read_from_file_in_directory_recursively


TEST_DIRECTORY = 'C:/x/tests'


def test_read_from_file_in_directory_recursively():
    before_each()
    os.mkdir(TEST_DIRECTORY + '/top')
    os.mkdir(TEST_DIRECTORY + '/top/nested')
    os.mkdir(TEST_DIRECTORY + '/top/nested/nestedagain')

    with open(TEST_DIRECTORY + '/file.txt', 'w') as f:
        f.write("one line\ntwo line\nthree line")
    
    with open(TEST_DIRECTORY + '/top/file.txt', 'w') as f:
        f.write("one line\ntwo line\nthree line")
    
    with open(TEST_DIRECTORY + '/top/file2.txt', 'w') as f:
        f.write("one line\ntwo line\nthree line")
    
    with open(TEST_DIRECTORY + '/top/nested/file.txt', 'w') as f:
        f.write("one line\ntwo line\nthree line")
    
    with open(TEST_DIRECTORY + '/top/nested/file2.txt', 'w') as f:
        f.write("one line\ntwo line\nthree line")
    
    actual = read_from_file_in_directory_recursively(TEST_DIRECTORY, [])
    expected = {
        'C:/x/tests/file.txt': 'one line\ntwo line\nthree line',
        'C:/x/tests/top/file.txt': 'one line\ntwo line\nthree line',
        'C:/x/tests/top/file2.txt': 'one line\ntwo line\nthree line',
        'C:/x/tests/top/nested/file.txt': 'one line\ntwo line\nthree line',
        'C:/x/tests/top/nested/file2.txt': 'one line\ntwo line\nthree line'
    }

    assert actual == expected
    after_each()
    

def after_each():
    setup_test_directory()


def before_each():
    setup_test_directory()


def setup_test_directory():
    if not os.path.isdir('C:'):
        os.mkdir('C:')

    if not os.path.isdir('C:/x'):
        os.mkdir('C:/x')
    
    if not os.path.isdir('C:/x/tests'):
        os.mkdir('C:/x/tests')
    
    shutil.rmtree(TEST_DIRECTORY)
    os.mkdir(TEST_DIRECTORY)
    
