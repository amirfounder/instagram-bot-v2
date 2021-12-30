import os
import shutil
from src.data_manager.files import read_from_file_in_directory_recursively, try_open
from time import sleep, time
from threading import Thread


TEST_DIRECTORY = 'C:/x/tests'

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
    

def test_try_open_file_given_file_closed_success():
    before_each()

    file_path = TEST_DIRECTORY + '/test.txt'
    file = try_open(file_path, 'w')
    file.write('test')
    file.close()

    file = try_open(file_path, 'r')
    content = file.read()
    file.close()

    assert content == 'test'
    after_each()


def test_try_open_file_given_file_opened_no_error():
    before_each()

    file_path = TEST_DIRECTORY + '/test.txt'

    state = { 'content': None }

    file = try_open(file_path, 'w')
    file.write('test')
    file.close()

    def open_file_2_seconds():
        file = try_open(file_path, 'r')
        sleep(2)
        file.close()

    def read_file(state):
        file = try_open(file_path, 'r')
        content = file.read()
        file.close()
        state['content'] = content
    
    t1 = Thread(target=open_file_2_seconds)
    t2 = Thread(target=read_file, args=(state,))

    start = time()

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time()

    assert end - start > 2
    assert state['content'] == 'test'

    after_each()

