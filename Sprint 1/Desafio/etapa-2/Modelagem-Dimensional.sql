CREATE VIEW DimCliente AS
SELECT
    c.idCliente AS idDimCliente,
    c.nomeCliente,
    c.cidadeCliente,
    c.estadoCliente,
    c.paisCliente
FROM CLIENTE c;

CREATE VIEW DimVendedor AS
SELECT
    v.idVendedor AS idDimVendedor,
    v.nomeVendedor,
    v.sexoVendedor,
    v.estadoVendedor
FROM VENDEDOR v;

CREATE VIEW DimCarro AS
SELECT
    ca.idCarro AS idDimCarro,
    ca.classiCarro,
    ca.marcaCarro,
    ca.modeloCarro,
    ca.anoCarro,
    ca.kmCarro,
    co.tipoCombustivel
FROM CARRO ca
JOIN COMBUSTIVEL co ON ca.idCombustivel = co.idCombustivel;

CREATE VIEW DimTempo AS
SELECT DISTINCT
    l.dataLocacao AS dataCompleta,
    strftime('%d', l.dataLocacao) AS dia,
    strftime('%m', l.dataLocacao) AS mes,
    strftime('%Y', l.dataLocacao) AS ano
FROM LOCACAO l

UNION

SELECT DISTINCT
    l.dataEntrega AS dataCompleta,
    strftime('%d', l.dataEntrega) AS dia,
    strftime('%m', l.dataEntrega) AS mes,
    strftime('%Y', l.dataEntrega) AS ano
FROM LOCACAO l
WHERE l.dataEntrega IS NOT NULL;

CREATE VIEW FactLocacao AS
SELECT
    lo.idLocacao   AS idFatoLocacao,
    lo.qtdDiaria,
    lo.vlrDiaria,
    lo.dataLocacao,
    lo.horaLocacao,
    lo.dataEntrega,
    lo.horaEntrega,
    lo.idCliente AS idDimCliente,
    lo.idCarro AS idDimCarro,
    lo.idVendedor AS idDimVendedor
FROM LOCACAO lo;
