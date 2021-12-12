import os


class FileManager():
  def __init__(
    self,
    target_file=None,
    target_directory=None,
    file_extension='.txt',
    max_file_size=25*1000*1000
    ):
    self.__target_file = target_file
    self.__target_directory = target_directory
    self.__file_extension = file_extension
    self.__max_file_size = max_file_size

  def write_bytearray_to_file(self, content, file):
    directory = '/'.join(file.split('/')[:-1])
    if not os.path.isdir(directory):
      self.build_directory(directory)
    
    f = open(file, 'wb')
    f.write(content)
    f.close()

  def write_to_directory(self, content, directory=None):
    if directory is None:
      directory = self.__target_directory
    
    if not os.path.isdir(directory):
      self.build_directory(directory)

    target_file_name = '1' + self.__file_extension
    
    files = [x for x in os.listdir(directory) if os.path.isfile(directory + '/' + x)]
    file_count = len(files)

    if file_count > 0:
      last_file = files[file_count - 1]
      last_file_size = os.path.getsize(directory + '/' + last_file)

      if last_file_size > self.__max_file_size:
        target_file_name = str(file_count + 1) + self.__file_extension
      else:
        target_file_name = last_file
    
    target_file_path = directory + '/' + target_file_name
    self.write_to_file(content, target_file_path)

  def write_to_file(self, content, file=None):
    if file is None:
      file = self.__target_file
    
    directory = '/'.join(file.split('/')[:-1])
    if not os.path.isdir(directory):
      self.build_directory(directory)
    
    f = open(file, 'a')
    f.write(content + '\n')
    f.close()
  
  def read_from_directory(self, directory=None):
    if directory is None:
      directory = self.__target_directory
    
    pass

  def read_from_file(self, file=None):
    if file is None:
      file = self.__target_file
    
    f = open(file, 'r')
    data = f.read()
    f.close()
    return data

  def build_directory(self, directory):
    directories = directory.split('/')
    current_dir = directories[0]
    directories = directories[1:]

    for directory in directories:
      if not os.path.isdir(current_dir + '/' + directory):
        os.mkdir(current_dir + '/' + directory)
      current_dir += '/' + directory
    