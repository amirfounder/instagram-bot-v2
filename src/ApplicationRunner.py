import os
from src import BotBuilder, FileManager, InteractionProxy


class ApplicationRunner():

  @staticmethod
  def run():
    # ApplicationRunner.run_sandbox()
    # ApplicationRunner.run_http_proxy()
    ApplicationRunner.run_content_builder()

  @staticmethod
  def run_http_proxy():
    os.system("mitmdump -s src/http_proxy/src/app.py --set console_eventlog_verbosity=error termlog_verbosity=error")
  
  @staticmethod
  def run_interaction_logger():
    pass
 
  @staticmethod
  def run_bot_builder():
    bot_builder = BotBuilder()
    bot_builder.build_bots()

  @staticmethod
  def run_content_builder():
    os.system('npm start')

  @staticmethod
  def run_interaction_proxy():
    interaction_proxy = InteractionProxy()
  
  @staticmethod
  def run_sandbox():
    file_manager = FileManager(target_directory='C:/x/logs/mitm-proxy/instagram/json')
    file_manager.write_to_directory('hello')