import os

from multiprocessing import Process, Value
from src import Bot, BotBuilder, DatabaseManager, \
  DataManager, InteractionAgent, Mouse
from src.builders.script_builder.src.JavascriptBuilder import JavascriptBuilder
from src.interaction_agent.src.agents.InstagramAgent import InstagramAgent
from src.console.src import Console \

def run() -> Value:
  
  os.system("mitmdump -s src/http_listener/listener.py --set console_eventlog_verbosity=error termlog_verbosity=error")




class ApplicationRunner():

  @staticmethod
  def run():
    ApplicationRunner.run_multiple([
      # ApplicationRunner.run_http_listener,
      ApplicationRunner.run_sandbox
      # ApplicationRunner.run_content_builder
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
    interaction_proxy = InteractionAgent()
    interaction_proxy.start()
  
  @staticmethod
  def run_sandbox():
    prompt = Console()

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
