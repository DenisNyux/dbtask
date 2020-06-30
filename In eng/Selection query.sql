CREATE TABLE Selection (
    [ID_пользователя] INTEGER NOT NULL
                              REFERENCES Users ([ID_Пользователя]) ON DELETE CASCADE
                                                                          ON UPDATE CASCADE,
    [ID_вакансии]     INTEGER NOT NULL
                              REFERENCES Vacancies ([ID_вакансии]) ON DELETE CASCADE
                                                                                 ON UPDATE CASCADE,
    Status            CHAR    NOT NULL,
    PRIMARY KEY (
        [ID_пользователя],
        [ID_вакансии]
    )
);

(SELECT [ID_вакансии] 
    FROM Selection 
    WHERE 
        [ID_пользователя] = 1 AND Status = 'True') 
AS Selection_vacancy 
INNER JOIN Vacancies ON 
    Vacancies.ID_вакансии = Selection_vacancy.ID_вакансии;