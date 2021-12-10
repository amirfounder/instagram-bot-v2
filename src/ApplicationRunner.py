import os
from time import sleep

from win32api import Sleep
from src import BotBuilder, InteractionProxy, System
from multiprocessing import Process
from src.interaction_proxy.src import proxies
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
    sleep(2)
    system = System()
    open_apps = system.get_open_apps()
    first_named_app = [x for x in open_apps if x[1] != ''][0][1]
    target_app = system.get_open_app_by_name(first_named_app)
    system.move_app_to_front(target_app)
    system.move_app_to_monitor(target_app, 1)
    sleep(1)
    system.move_app_to_monitor(target_app, 2)
    sleep(1)
    system.move_app_to_monitor(target_app, 3)
    # sleep(1)
    # system.move_app_to_monitor(target_app, 2)


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
