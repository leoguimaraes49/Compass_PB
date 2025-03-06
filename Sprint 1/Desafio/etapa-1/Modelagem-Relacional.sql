SELECT * FROM tb_locacao LIMIT 10;

CREATE TABLE CLIENTE (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(50),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);

CREATE TABLE COMBUSTIVEL (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(30)
);

CREATE TABLE CARRO (
    idCarro INT PRIMARY KEY,
    kmCarro int,
    classiCarro VARCHAR(30),
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES COMBUSTIVEL(idCombustivel)
);

CREATE TABLE VENDEDOR (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(50),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(50)
);

CREATE TABLE LOCACAO (
    idLocacao INT PRIMARY KEY,
    dataLocacao DATE,
    horaLocacao VARCHAR(5),
    dataEntrega DATE,
    horaEntrega VARCHAR(5),
    qtdDiaria INT,
    vlrDiaria DECIMAL(10,2),
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES CLIENTE(idCliente),
    FOREIGN KEY (idCarro) REFERENCES CARRO(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES VENDEDOR(idVendedor)
);


INSERT INTO CLIENTE (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

INSERT INTO COMBUSTIVEL (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

INSERT INTO CARRO (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, kmCarro, idCombustivel)
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, MAX(kmCarro), idCombustivel
FROM tb_locacao;

INSERT INTO VENDEDOR (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

INSERT INTO LOCACAO (
    idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria, 
    idCliente, idCarro, idVendedor
)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria, 
    idCliente, idCarro, idVendedor
FROM tb_locacao;


