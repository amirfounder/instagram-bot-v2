import os

from src import BotBuilder, InteractionProxy, InstagramProxy
from multiprocessing import Process
from src.utils.constants import BRAVE_EXECUTEABLE, LOTRO_APP_NAME


class ApplicationRunner():

  @staticmethod
  def run():
    ApplicationRunner.run_multiple([
      # ApplicationRunner.run_interaction_proxy,
      # ApplicationRunner.run_http_proxy,
      # ApplicationRunner.run_content_builder
      ApplicationRunner.run_sandbox()
    ])
  
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
    interaction_proxy.research_hashtags()
  
  @staticmethod
  def run_sandbox():
    proxy = InstagramProxy()
    proxy.start()
    proxy.research_hashtags()
    proxy._close_browser()

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
