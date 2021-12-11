from src.data_manager.src.FileManager import FileManager

from random import Random
import datetime
import string
import os
import secrets


class BotBuilder:

  def __init__(self) -> None:
    self.__target_directory = 'C:\\x\\bots'
    self.__file_manager = FileManager()
    self.__rand = Random()
  
  def convert_to_csv_format(self, csv_rows_rows: list[list[str]]):
    return '\n'.join([','.join(row) for row in csv_rows_rows])

  def build_bots(self, save_to_file=True) -> list[list[str]]:
    bot_factory_parts_directory = 'C:/x/bots/bot_factory_parts'

    firstnames_boy = self.__file_manager.read_from_file(bot_factory_parts_directory + '/firstnames_boy.txt').split('\n')
    firstnames_girl = self.__file_manager.read_from_file(bot_factory_parts_directory + '/firstnames_girl.txt').split('\n')
    lastnames = self.__file_manager.read_from_file(bot_factory_parts_directory + '/lastnames.txt').split('\n')
    
    firstnames = firstnames_boy + firstnames_girl

    csv_headers = ['first_name', 'last_name', 'gender', 'birthday', 'username', 'password']
    csv_rows_rows = [csv_headers]

    for i in range(len(firstnames)):
      firstname = firstnames[i]
      gender = 'M' if i <= len(firstnames_boy) else 'F'

      for lastname in lastnames:
        birthday = self.build_birthday()
        username = self.build_username(firstname, lastname)
        password = self.build_password()

        row = [firstname, lastname, gender, birthday, username, password]
        csv_rows_rows.append(row)
      
      if i % (len(firstnames) / 20) == 0:
        print(f'completed: {int(i / len(firstnames) * 100)}%')

    if save_to_file:
      self.save_bots_to_file(csv_rows_rows)

    return csv_rows_rows
    
  def build_username(self, firstname, lastname):
    random_int = self.__rand.randint(10000, 99999)
    random_int = str(random_int)
    return f'{firstname}{lastname}{random_int}'

  def build_password(self, length=12):
    letters = string.ascii_letters
    numbers = '0123456789'
    special = '!@#$%^&*()'

    chars = letters + numbers + special
    chars = list(chars)

    return ''.join([secrets.choice(chars) for x in range(length)])
  
  def build_birthday(self):
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2001, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = self.__rand.randrange(days_between_dates)

    birthday = start_date + datetime.timedelta(days=random_number_of_days)
    return str(birthday)
  
  def save_bots_to_file(self, csv_rows_rows):
    files = [x for x in os.listdir(self.__target_directory) if os.path.isfile(self.__target_directory + '/' + x)]
    target_file = f'{self.__target_directory}\\bots_v{len(files)}.csv'
    content = self.convert_to_csv_format(csv_rows_rows)
    self.__file_manager.write_to_file(content, target_file)