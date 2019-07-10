CREATE TABLE Parametrizacoes (
    Id INT NOT NULL,
    Tensao DOUBLE NOT NULL,
    Correntem DOUBLE NOT NULL,
    Tempo DOUBLE NOT NULL,
    MGycm DOUBLE NOT NULL,
    Tamanho CHAR(1) NOT NULL, -- 'T', 'S', 'M', 'B'
    PRIMARY KEY (Id)
);