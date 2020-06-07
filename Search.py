import sqlite3


# Paths to db`s
VACANCY = '.\Вакансии.db'
COMPANIES = '.\Компании.db'
COMMON = '.\Общее.db'
UNEMPLOYED = '.\Соискатель.db'


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