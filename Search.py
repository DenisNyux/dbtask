import sqlite3

BASE_PATH = './Base.db'
   
class SearchApp:

    __exact_user = None


    def __init__(self):
        while self.__exact_user == None:
            print('Введите свой логин и пароль для доступа')
            log = input('Логин: ')
            pas = input('Пароль: ')
            self.log_in(log, pas)
        

    def __establish_connection(self, path_to_db):
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


    def log_in(self, log, pas):
        query = "SELECT * FROM [Пользователи] WHERE [Логин] = " + "'" + log + "'" "AND [Пароль] = "+ "'" + pas + "'"
        user = self.__establish_connection(BASE_PATH)['cursor'].execute(query).fetchall()
        if user:
            print('Авторизация прошла успешно')
            self.__exact_user = user[0]
        else: 
            print('Такого пользователя нет. Попробуйте еще раз.')

    
    
    

# print('Введите свой логин и пароль для доступа')
# log = input('Логин: ')
# pas = input('Пароль: ')
app = SearchApp()    
# print(app.log_in(log, pas))





# conn = establish_connection(BASE_PATH)
# cur = conn['cursor']
# a = cur.execute('SELECT * FROM [Пользователи]').fetchall()
# print(a)


# def regexp(expr, item):
#     reg = re.compile(expr)
#     return reg.search(item) is not None

# def add_data(connection, table_name, data):
#     # try:
#     connection['conn'].create_function("REGEXP", 2, regexp)
