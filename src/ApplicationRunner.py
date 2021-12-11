import os

from multiprocessing import Process
from src import Bot, BotBuilder, DatabaseManager, \
  DataManager, InteractionProxy, Mouse
from src.builders.script_builder.src.JavascriptBuilder import JavascriptBuilder
from src.interaction_proxy.src.proxies.InstagramProxy import InstagramProxy \


class ApplicationRunner():

  @staticmethod
  def run():
    ApplicationRunner.run_multiple([
      # ApplicationRunner.run_http_listener,
      ApplicationRunner.run_sandbox
    ])
  
  @staticmethod
  def run_data_manager():
    data_manager = DataManager()
    data_manager.run()
    pass

  @staticmethod
  def run_http_listener():
    os.system("mitmdump -s src/http_listener/src/app.py --set console_eventlog_verbosity=error termlog_verbosity=error")
  
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
    interaction_proxy.research_hashtags()
  
  @staticmethod
  def run_sandbox():
    x = InstagramProxy()
    x.start()
    x.login()

  @staticmethod
  def run_multiple(processes):
    runners = []

    for process in processes:
      runner = Process(target=process)
      runners.append(runner)
    
    for runner in runners:
      runner.start()
    
    for runner in runners:
      runner.join()
