CREATE TABLE Cefalogramas (
    Id INT NOT NULL,
    PacienteId INT NOT NULL,
    Valor DOUBLE,
    DataDeEntrega DATETIME,
    MotivoExame VARCHAR(255),
    ParametrizacaoId INT NOT NULL,
    Modelo INT NOT NULL, -- 1..4

    TipoPanoramica VARCHAR (30) NOT NULL, -- 'Normal', 'Infantil', 'Implantes', 'Telerradiografia Lateral', 'Telerradiografia Frontal', 'Radiografia Carpal', 'Radiografia Atm Planigrafia', 'Radiografia Seios Maxilares'
    Especializacao VARCHAR (15), -- 'Topo', 'Oclusao', 'Idade Ossea'
    Regiao VARCHAR(50),
    Modelo INT, -- 1..9
    PRIMARY KEY (Id),



        public ModeloCefalograma Modelo { get; set; }
        public int Medida { get; set; }




    INDEX pac_cef_ind (PacienteId),
    FOREIGN KEY (PacienteId)
        REFERENCES Pacientes (Id)
        ON DELETE CASCADE,
    INDEX par_cef_ind (ParametrizacaoId),
    FOREIGN KEY (ParametrizacaoId)
        REFERENCES Parametrizacoes (Id)
        ON DELETE CASCADE
);