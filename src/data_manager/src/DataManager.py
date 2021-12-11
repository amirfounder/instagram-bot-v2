from src.data_manager.src.FileManager import FileManager
from src.data_manager.src.BackupManager import BackupManager
from src.data_manager.src.database import DatabaseManager

class DataManager:

  def __init__(self):
    self.__file_manager = FileManager()
    self.__database_manager = DatabaseManager()
    self.__backup_manager = BackupManager()

  def run():
    pass

  def sync_todays_files_with_database(self):
    pass