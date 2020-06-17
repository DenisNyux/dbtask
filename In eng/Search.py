import sqlite3

# прересечение резюме с вакансиями


BASE_PATH = './Base.db'
   
class SearchApp:

    __user_type = None
    __user_id = None

    def __init__(self):
        while self.__user_id == None:
            print('Введите свой логин и пароль для доступа')
            log = input('Логин: ')
            pas = input('Пароль: ')
            self.__log_in(log, pas)
        if self.__user_type == 2:
            self.__company_interface()
        else:
            self.__user_interface()


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


    def __log_in(self, log, pas):
        query = "SELECT * FROM Users WHERE Логин = " + "'" + log + "'" "AND Пароль = "+ "'" + pas + "'"
        user = self.__establish_connection(BASE_PATH)['cursor'].execute(query).fetchall()
        if user:
            print('Авторизация прошла успешно')
            self.__user_type = user[0][3]
            self.__user_id = user[0][0]
        else: 
            print('Такого пользователя нет. Попробуйте еще раз.')

    
    def __company_interface(self):
        choice = None
        while not(choice):
            choice = input('Создать новую вакансию?\n\n1) Да\n2) Нет')
            if choice == 1:
                self.enter_vacancy()
            elif choice == 2:
                pass
            else:
                choice = None

    def enter_vacancy(self):
        pass


    def __user_interface(self):
        choice = None
        while not(choice):
            choice = input('Найти вакансии?\n\n1) Да\n2) Нет\n')
            if choice == '1':
                self.make_search()
            elif choice == '2':
                pass
            else:
                choice = None

    def make_search(self):
        connection_obj = self.__establish_connection(BASE_PATH)
                   
        



app = SearchApp()    





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
#def make_search(self):
    #     connection_obj = self.__establish_connection(BASE_PATH)
    #     finder_id = connection_obj['cursor'].execute(
    #         f'''SELECT ID соискателя FROM [Информация о соискателе] WHERE [ID пользователя] = {self.__user_id};'''
    #     ).fetchall()[0][0]
    #     # all_vacancies = connection_obj['cursor'].execute('''SELECT * FROM [Информация о вакансии];''').fetchall()

    #     # Compare skills
    #     user_skills = connection_obj['cursor'].execute(
    #         f'''SELECT [ID навыка] FROM [Соискатель навыки] WHERE [ID соискателя] = {finder_id};'''
    #     ).fetchall()
    #     vacancies_skills = connection_obj['cursor'].execute(
    #         f'''SELECT * FROM [Вакансия навыки];'''
    #     ).fetchall()
    #     print(user_skills, vacancies_skills)



# finder_id = connection_obj['cursor'].execute(
#             f'''SELECT ID_соискателя FROM Finder WHERE ID_пользователя = {self.__user_id};'''
#         ).fetchall()[0][0]
        
    # Compare skills
        # user_skills = connection_obj['cursor'].execute(
        #     f'''SELECT * FROM Finder_skills WHERE ID_соискателя = {finder_id};'''
        # ).fetchall()
        # company_skills = connection_obj['cursor'].execute(
        #     f'''SELECT * FROM Vacancy_skills ORDER BY ID_вакансии;'''
        # ).fetchall()
        # usr_skill_lst = [i[1] for i in user_skills]
        # # Compare requirements
        # finder_reqs = connection_obj['cursor'].execute(
        #     f'''SELECT Страна, Город, Гражданство_РФ, Прописка FROM Finder_requirements WHERE ID_соискателя = {finder_id};'''
        # ).fetchall()
        # print(user_skills, company_skills)
        # # Compare languages