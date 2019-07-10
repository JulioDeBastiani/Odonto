CREATE TABLE Cefalogramas (
    Id INT NOT NULL,
    PacienteId INT NOT NULL,
    Valor DOUBLE,
    DataDeEntrega DATETIME,
    MotivoExame VARCHAR(255),
    ParametrizacaoId INT NOT NULL,
    Modelo INT NOT NULL, -- 1..4
    PRIMARY KEY (Id),
    INDEX pac_cef_ind (PacienteId),
    FOREIGN KEY (PacienteId)
        REFERENCES Pacientes (Id)
        ON DELETE CASCADE,
    INDEX par_cef_ind (ParametrizacaoId),
    FOREIGN KEY (ParametrizacaoId)
        REFERENCES Parametrizacoes (Id)
        ON DELETE CASCADE
);