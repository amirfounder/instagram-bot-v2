"""TODO
"""
import os
from src.utils.constants import MAX_LOG_FILE_SIZE


def read_from_file_in_directory_recursively(path: str):
    pass


def read_from_files_in_directory(directory: str):
    contents = os.listdir(directory)
    content_paths = ['{}/{}'.format(directory, x) for x in contents]
    
    paths = [x for x in content_paths if is_file(x)]

    return read_from_files(paths)


def read_from_files(paths: list[str]):
    data_map = {}

    for path in paths:
        data = read_from_file(path)
        data_map[path] = data
    
    return data_map


def read_from_file(path: str):
    data = None

    with open(path, 'r') as f:
        data = f.read()

    return data


def append_to_file_in_directory(directory: str, content: str):
    file = None
    
    if not is_directory(directory):
        create_directories(directory)
        file = '{}/1.txt'.format(directory)
    else:
        file = get_next_file_in_directory(directory)
    
    append_to_file(file, content)


def append_to_file(path: str, content: str):
    directory = get_file_directory(path)
    if not is_directory(directory):
        create_directories(directory)
    
    with open(path, 'a') as f:
        f.write(content)


def get_next_file_in_directory(directory: str): 
    contents = os.listdir(directory)
    files = [x for x in contents if is_file('{}/{}'.format(directory, x))]
    files_count = len(files)

    if files_count == 0:
        return '{}/1.txt'.format(directory)
    
    last_file_name = files[files_count - 1]
    last_file_path = '{}/{}'.format(directory, last_file_name)
    last_file_size = os.path.getsize(last_file_path)

    if last_file_size < MAX_LOG_FILE_SIZE:
        return last_file_path

    return '{}/{}.txt'.format(directory, files_count + 1)


def save_bytes_to_image_in_directory(directory: str, content: bytes, name: str):
    if not is_directory(directory):
        create_directories(directory)
    
    path = '{}/{}'.format(directory, name)
    save_bytes_to_image(path, content)


def save_bytes_to_image(path: str, content: bytearray):  
    directory = get_file_directory(path)
    if not is_directory(directory):
        create_directories(directory)
    
    with open(path, 'wb') as f:
        f.write(content)


def create_file(path: str):
    open(path, 'x').close()


def is_file(path: str):
    return os.path.isfile(path)


def is_directory(path: str):
    return os.path.isdir(path)


def get_file_directory(path: str):
    if is_directory(path):
        return path

    dir_paths = path.split('/')[:-1]
    directory = '/'.join(dir_paths)

    return directory


def create_directories(path: str):
    dir_paths = path.split('/')
    current = dir_paths[0]
    dir_paths = dir_paths[1:]

    for directory in dir_paths:
      if not os.path.isdir(current + '/' + directory):
        os.mkdir(current + '/' + directory)
      current += '/' + directory