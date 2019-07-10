CREATE TABLE Tomografias (
    Id INT NOT NULL,
    PacienteId INT NOT NULL,
    Valor DOUBLE,
    DataDeEntrega DATETIME,
    MotivoExame VARCHAR(255),
    ParametrizacaoId INT NOT NULL,
    Tipo VARCHAR(10) NOT NULL, -- 'Maxila', 'Mandibula', 'ATM', 'Segmento', 'Elemento'
    Especializacao VARCHAR(20), -- 'Ramos Mandibulares', 'Oclusao', 'Abertura'
    Regiao VARCHAR(50),
    Elemento VARCHAR(50),
    Proporcao VARCHAR(5) NOT NULL, -- '5x5', '6x8', '8x8', '8x15', '13x15'
    Alvo VARCHAR(5) NOT NULL, -- 'Alvo', 'Dente'
    Resolucao CHAR(1) NOT NULL, -- 'B', 'M', 'A'
    PRIMARY KEY (Id),
    INDEX pac_tom_ind (PacienteId),
    FOREIGN KEY (PacienteId)
        REFERENCES Pacientes (Id)
        ON DELETE CASCADE,
    INDEX par_tom_ind (ParametrizacaoId),
    FOREIGN KEY (ParametrizacaoId)
        REFERENCES Parametrizacoes (Id)
        ON DELETE CASCADE
);