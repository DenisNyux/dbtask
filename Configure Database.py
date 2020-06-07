"""Функции для осуществления CRUD с базами данных"""

import sqlite3
import re

# Paths to db`s
VACANCY = '.\Вакансии.db'
COMPANIES = '.\Компании.db'
COMMON = '.\Общее.db'
UNEMPLOYED = '.\Соискатель.db'


def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def establish_connection(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}
    return connection


def show_all_tables(connection):
    return connection['cursor'].execute('''SELECT * FROM sqlite_master WHERE type = 'table' ''').fetchall()


def show_exact_table(connection, table_name):
    return connection['cursor'].execute(f'''SELECT * FROM {table_name} ''').fetchall()


def add_data(connection, table_name, data):
    # try:
    connection['conn'].create_function("REGEXP", 2, regexp)
    connection['cursor'].execute(f'''INSERT INTO {table_name} VALUES {str(data)}''')
    connection['conn'].commit()
    # except sqlite3.Error as e:
    #     print(f'Error occured with adding users to db. {e}')


def delete_data_by_cond(connection, table_name, cond):
    connection['cursor'].execute(f'''DELETE FROM {table_name} WHERE {cond}''')
    connection['conn'].commit()

# print(establish_connection(VACANCY))
# print(*show_all_tables(establish_connection(VACANCY)), sep='\n\n')
# add_data(establish_connection(UNEMPLOYED), '[Информация о соискателе]', (4, 'Царулкова', 'Анастасия', 'Витальевна', '06.07.2000', 'asa@asa.ru', '+80987654309', 'Целеустремленная, креативная', 2))
print(*show_exact_table(establish_connection(UNEMPLOYED), '[Информация о соискателе]'), sep='\n\n')
cond = '''[ID соискателя] = 3'''
delete_data_by_cond(establish_connection(UNEMPLOYED), '[Информация о соискателе]', cond)
print(*show_exact_table(establish_connection(UNEMPLOYED), '[Информация о соискателе]'), sep='\n\n')
