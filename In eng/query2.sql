INSERT INTO Search_result
SELECT Vacancies.ID_вакансии,
       (
           SELECT Companies.Название_компании
             FROM Companies
            WHERE Companies.ID_компании = Vacancies.ID_компании
       )
       AS Компания,
       (
           SELECT Fields.[Название раздела]
             FROM Fields
            WHERE Fields.ID_раздела = Vacancies.ID_раздела
       )
       AS Раздел,
       Vacancies.Зарплата,
       Vacancies.Опыт_работы,
       Vacancies.Тип_занятости,
       Vacancy_requirements.Гражданство,
       Vacancy_requirements.Прописка,
       Vacancy_requirements.Личные_качества,
       Vacancy_requirements.Форма_образования
  FROM Vacancies
       INNER JOIN
       Vacancy_requirements ON Vacancies.ID_вакансии = Vacancy_requirements.ID_вакансии;