-- 📌 EXERCÍCIOS REFERENTES AO SCHEMA BIBLIOTECA

-- E01 - Listar todos os livros publicados após 2014
-- Apresente a query para listar todos os livros publicados após 2014.
-- Ordenar pela coluna cod, em ordem crescente.
-- Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
FROM LIVRO
WHERE publicacao > '2014-12-31'
ORDER BY cod ASC;

-- E02 - Listar os 10 livros mais caros
-- Apresente a query para listar os 10 livros mais caros.
-- Ordenar as linhas pela coluna valor, em ordem decrescente.
-- Atenção às colunas esperadas no resultado final: titulo, valor.

SELECT titulo, valor
FROM LIVRO
ORDER BY valor DESC
LIMIT 10;

-- E03 - Listar as 5 editoras com mais livros na biblioteca
-- Apresente a query para listar as 5 editoras com mais livros na biblioteca.
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

SELECT COUNT(L.cod) AS quantidade, E.nome, EN.estado, EN.cidade
FROM LIVRO L
JOIN EDITORA E ON L.editora = E.codEditora
JOIN ENDERECO EN ON E.endereco = EN.codEndereco
GROUP BY E.codEditora
ORDER BY quantidade DESC
LIMIT 5;

-- E04 - Quantidade de livros publicados por cada autor
-- Apresente a query para listar a quantidade de livros publicada por cada autor.
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente.
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

SELECT autor.codAutor, autor.nome, autor.nascimento, 
       COALESCE(COUNT(livro.cod), 0) AS quantidade
FROM autor
LEFT JOIN livro ON autor.codAutor = livro.autor
GROUP BY autor.codAutor, autor.nome, autor.nascimento
ORDER BY autor.nome ASC;

-- E05 - Listar autores que publicaram fora da região Sul do Brasil
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região Sul do Brasil.
-- Ordene o resultado pela coluna nome, em ordem crescente.
-- Não podem haver nomes repetidos em seu retorno.

SELECT DISTINCT A.nome
FROM AUTOR A
JOIN LIVRO L ON A.codAutor = L.autor
JOIN EDITORA E ON L.editora = E.codEditora
JOIN ENDERECO EN ON E.endereco = EN.codEndereco
WHERE EN.estado NOT IN ('PR', 'SC', 'RS')
ORDER BY A.nome ASC;

-- E06 - Autor com maior número de livros publicados
-- Apresente a query para listar o autor com maior número de livros publicados.
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

SELECT A.codAutor, A.nome, COUNT(L.cod) AS quantidade_publicacoes
FROM AUTOR A
JOIN LIVRO L ON A.codAutor = L.autor
GROUP BY A.codAutor
ORDER BY quantidade_publicacoes DESC
LIMIT 1;

-- E07 - Listar os autores sem nenhuma publicação
-- Apresente a query para listar o nome dos autores com nenhuma publicação.
-- Apresentá-los em ordem crescente.

SELECT A.nome
FROM AUTOR A
LEFT JOIN LIVRO L ON A.codAutor = L.autor
WHERE L.cod IS NULL
ORDER BY A.nome ASC;

-- 📌 EXERCÍCIOS REFERENTES AO SCHEMA LOJA

-- E08 - Vendedor com maior número de vendas concluídas
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),
-- considerando apenas as vendas com status 'Concluído'.
-- As colunas presentes no resultado devem ser cdvdd e nmvdd.

SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
JOIN tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY COUNT(tbvendas.cdven) DESC
LIMIT 1;

-- E09 - Produto mais vendido entre 2014-02-03 e 2018-02-02
-- Apresente a query para listar o código e nome do produto mais vendido no período especificado,
-- considerando apenas vendas com status 'Concluído'.
-- As colunas presentes no resultado devem ser cdpro e nmpro.

SELECT tbvendas.cdpro, tbvendas.nmpro
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
AND tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY tbvendas.cdpro, tbvendas.nmpro
ORDER BY SUM(tbvendas.qtd) DESC
LIMIT 1;

-- E10 - Cálculo da comissão dos vendedores
-- A comissão de um vendedor é definida com base no percentual sobre o total de vendas realizadas (quantidade * valor unitário).
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, na tabela tbvendedor.
-- Apresente a query para calcular a comissão de todos os vendedores, considerando apenas vendas concluídas.
-- As colunas no resultado devem ser vendedor, valor_total_vendas e comissao.
-- A comissão deve ser apresentada em ordem decrescente e arredondada para duas casas decimais.

SELECT 
    tbvendedor.nmvdd AS vendedor, 
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100, 2) AS comissao
FROM tbvendas
JOIN tbvendedor ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.nmvdd, tbvendedor.perccomissao
ORDER BY comissao DESC;

-- E11 - Cliente com maior gasto na loja
-- Apresente a query para listar o código e nome do cliente com maior gasto na loja.
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto (total de compras do cliente em vendas concluídas).

SELECT tbvendas.cdcli, tbvendas.nmcli, 
       ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS gasto
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.cdcli, tbvendas.nmcli
ORDER BY gasto DESC
LIMIT 1;

-- E12 - Dependentes do vendedor com menor valor bruto de vendas (não sendo zero)
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor 
-- que teve o menor valor total bruto de vendas (não sendo zero).
-- As colunas esperadas no resultado são: cddep, nmdep, dtnasc e valor_total_vendas.
-- Considerar apenas vendas concluídas.

SELECT tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc, vendas.valor_total_vendas
FROM tbdependente
JOIN (
    SELECT tbvendas.cdvdd, 
           ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS valor_total_vendas
    FROM tbvendas
    WHERE tbvendas.status = 'Concluído'
    GROUP BY tbvendas.cdvdd
    HAVING valor_total_vendas > 0
    ORDER BY valor_total_vendas ASC
    LIMIT 1
) AS vendas ON tbdependente.cdvdd = vendas.cdvdd;

-- E13 - Listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de 'E-Commerce' ou 'Matriz'.
-- Considerar apenas vendas concluídas.
-- As colunas esperadas no resultado são: cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro, 
       SUM(tbvendas.qtd) AS quantidade_vendas
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
AND tbvendas.nmcanalvendas IN ('E-Commerce', 'Matriz')
GROUP BY tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10;

-- E14 - Gasto médio por estado
-- Apresente a query para listar o gasto médio por estado da federação.
-- As colunas esperadas no resultado são: estado e gastomedio.
-- O valor da coluna gastomedio deve ser arredondado para duas casas decimais e ordenado em ordem decrescente.
-- Considerar apenas vendas concluídas.

SELECT tbvendas.estado, 
       ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) AS gastomedio
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.estado
ORDER BY gastomedio DESC;

-- E15 - Listar códigos das vendas deletadas
-- Apresente a query para listar os códigos das vendas identificadas como deletadas.
-- O resultado deve ser apresentado em ordem crescente.

SELECT tbvendas.cdven
FROM tbvendas
WHERE tbvendas.deletado = 1
ORDER BY tbvendas.cdven;

-- E16 - Quantidade média vendida de cada produto por estado da federação
-- Apresente a query para listar a quantidade média vendida de cada produto, agrupado por estado da federação.
-- As colunas esperadas no resultado são: estado, nmpro e quantidade_media.
-- O valor da coluna quantidade_media deve ser arredondado para quatro casas decimais.
-- Os resultados devem ser ordenados pelo estado (1º) e nome do produto (2º).
-- Considerar apenas vendas concluídas.

SELECT tbvendas.estado, 
       tbvendas.nmpro, 
       ROUND(AVG(tbvendas.qtd), 4) AS quantidade_media
FROM tbvendas
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendas.estado, tbvendas.nmpro
ORDER BY tbvendas.estado ASC, tbvendas.nmpro ASC;
