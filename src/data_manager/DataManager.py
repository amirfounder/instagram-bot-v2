from src.data_manager.src.FileManager import FileManager
from src.data_manager.src.BackupManager import BackupManager
from src.data_manager.src.database import DatabaseManager

class DataManager:

  def __init__(self):
    self.__file_manager = FileManager()
    self.__database_manager = DatabaseManager()
    self.__backup_manager = BackupManager()

  def run(self):
    self.run_syncs()
    self.run_backups()

  def run_syncs(self):
    pass

  def run_backups(self):
    pass

  def sync_http_requests(self):
    pass

  def sync_bots(self):
    pass
