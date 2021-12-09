import os
from time import sleep
from src import BotBuilder, FileManager, InteractionProxy, System
from multiprocessing import Process
from src.interaction_proxy.src import proxies

from src.interaction_proxy.src.proxies.base.BrowserProxy import BrowserProxy
from src.interaction_proxy.src.proxies.specialized import InstagramProxy


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
  def run_assistant():
    pass

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
    system = System()
    apps = system.get_open_apps()
    lotro = None
    for app in apps:
      _, name = app
      if name == 'The Lord of the Rings Online™':
        lotro = app
        break
    if lotro is None:
      return
    system.show_window_normal(lotro[0])
    sleep(1)
  
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
