CREATE TABLE Clientes(

	idCliente INTEGER PRIMARY KEY ,
	nomeCliente TEXT,
	cidadeCliente TEXT,
	estadoCliente TEXT,
	paisCliente TEXT
)
	
CREATE TABLE Carros (
    idCarro INTEGER PRIMARY KEY,
    kmCarro INTEGER,
    classiCarro TEXT,
    marcaCarro TEXT,
    modeloCarro TEXT,
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES Combustiveis(idCombustivel)
)

CREATE TABLE Combustiveis (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TEXT
)

CREATE TABLE Vendedores (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor TEXT,
    sexoVendedor INTEGER,
    estadoVendedor TEXT
)

CREATE TABLE Locacoes (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INTEGER,
    vlrDiaria DECIMAL(10, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INTEGER,
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)
)

INSERT INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao ;

INSERT INTO Combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

INSERT INTO Locacoes (idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

INSERT INTO Carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;

INSERT INTO Carros (idCarro)
SELECT idCarro FROM tb_locacao 

DELETE FROM tb_locacao 
WHERE idCarro IN (
    SELECT idCarro
    FROM tb_locacao 
    GROUP BY idCarro
    HAVING COUNT(idCarro) > 1
)
AND ROWID NOT IN (
    SELECT MIN(ROWID)
    FROM tb_locacao
    GROUP BY idCarro
    HAVING COUNT(idCarro) > 1
);

SELECT * from Locacoes l 

SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;
