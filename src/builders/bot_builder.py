from src.data_manager.files import get_files_from_directory, read_from_file, append_to_file

from random import Random
import datetime
import string
import secrets

BOT_DIRECTORY = 'C:/x/bots'
BOT_FACTORY_PARTS_DIRECTORY = '{}/bot_factory_parts'.format(BOT_DIRECTORY)

random = Random()


def build_bots():
    firstnames_boy = read_from_file(
        '{}/firstnames_boy.txt'.format(BOT_FACTORY_PARTS_DIRECTORY)).split('\n')
    firstnames_girl = read_from_file(
        '{}/firstnames_girl.txt'.format(BOT_FACTORY_PARTS_DIRECTORY)).split('\n')
    lastnames = read_from_file(
        '{}/lastnames.txt'.format(BOT_FACTORY_PARTS_DIRECTORY)).split('\n')

    firstnames = firstnames_boy + firstnames_girl

    header = [
        'first_name',
        'last_name',
        'gender',
        'birthday',
        'username',
        'password'
    ]

    data = [header]

    for i in range(len(firstnames)):
        firstname = firstnames[i]
        gender = 'M' if i <= len(firstnames_boy) else 'F'

        for lastname in lastnames:
            birthday = build_birthday()
            username = build_username(firstname, lastname)
            password = build_password(12)

            row = [firstname, lastname, gender,
                   birthday, username, password]
            data.append(row)

    return data


def build_username(firstname: str, lastname: str):
    random_int = random.randint(10000, 99999)
    random_int = str(random_int)
    return '{}{}{}'.format(firstname, lastname, random_int)


def build_password(length: int):
    letters = string.ascii_letters
    numbers = '0123456789'
    special = '!@#$%^&*()'

    chars = letters + numbers + special
    chars = list(chars)

    return ''.join([secrets.choice(chars) for _ in range(length)])


def build_birthday():
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2001, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    birthday = start_date + datetime.timedelta(days=random_number_of_days)
    return str(birthday)


def format_csv_rows_of_rows_as_csv(data: list[list[str]]):
    records = [','.join(row) for row in data]
    return '\n'.join(records)


def save_bots_to_file(data: str):
    files = get_files_from_directory(BOT_DIRECTORY)
    files_count = len(files)

    file = '{}/{}.csv'.format(BOT_DIRECTORY, files_count)

    append_to_file(file, data)
