CREATE TABLE Pacientes (
    Id INT NOT NULL,
    Nome VARCHAR(255) NOT NULL,
    Nascimento DATE NOT NULL,
    ClinViewId VARCHAR(50),
    AlunoId INT,
    IndicacaoId INT,
    PRIMARY KEY (Id),
    INDEX al_ind (AlunoId),
    FOREIGN KEY (AlunoId)
        REFERENCES Alunos (Id)
        ON DELETE CASCADE,
    INDEX ind_ind (IndicacaoId),
    FOREIGN KEY (IndicacaoId)
        REFERENCES Indicacoes (Id)
        ON DELETE CASCADE
);