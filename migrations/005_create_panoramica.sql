CREATE TABLE Panoramicas (
    Id INT NOT NULL,
    PacienteId INT NOT NULL,
    Valor DOUBLE,
    DataDeEntrega DATETIME,
    MotivoExame VARCHAR(255),
    ParametrizacaoId INT NOT NULL,
    TipoPanoramica VARCHAR (30) NOT NULL, -- 'Normal', 'Infantil', 'Implantes', 'Telerradiografia Lateral', 'Telerradiografia Frontal', 'Radiografia Carpal', 'Radiografia Atm Planigrafia', 'Radiografia Seios Maxilares'
    Especializacao VARCHAR (15), -- 'Topo', 'Oclusao', 'Idade Ossea'
    Regiao VARCHAR(50),
    Modelo INT, -- 1..9
    PRIMARY KEY (Id),
    INDEX pac_pan_ind (PacienteId),
    FOREIGN KEY (PacienteId)
        REFERENCES Pacientes (Id)
        ON DELETE CASCADE,
    INDEX par_pan_ind (ParametrizacaoId),
    FOREIGN KEY (ParametrizacaoId)
        REFERENCES Parametrizacoes (Id)
        ON DELETE CASCADE
);