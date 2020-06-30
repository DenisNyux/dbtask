CREATE TABLE Выборка (
    [ID пользователя] INTEGER NOT NULL
                              REFERENCES Пользователи ([ID Пользователя]) ON DELETE CASCADE
                                                                          ON UPDATE CASCADE,
    [ID вакансии]     INTEGER NOT NULL
                              REFERENCES [Информация о вакансии] ([ID вакансии]) ON DELETE CASCADE
                                                                                 ON UPDATE CASCADE,
    Статус            CHAR    NOT NULL,
    PRIMARY KEY (
        [ID пользователя],
        [ID вакансии]
    )
);


(SELECT [ID вакансии] 
    FROM Выборка 
    WHERE 
        [ID пользователя] = 1 AND Статус = 'True') 
AS Выборка_вакансий 
INNER JOIN [Информация о вакансии] ON 
    [Информация о вакансии]."ID вакансии" = [Выборка_вакансий]."ID вакансии";
