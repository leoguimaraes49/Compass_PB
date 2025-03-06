# Instrução  

Este arquivo será o relato da minha entrega. Neste arquivo, faço a organização geral ao longo da Sprint. Aqui serão apresentadas as seções de aprendizado, exercícios e evidências da execução dos códigos.  

---

# Resumo  

### **SQL**  
Durante esta Sprint, aprendi a trabalhar com **consultas SQL mais avançadas**, utilizando diferentes formas de manipulação de dados. Desenvolvi habilidades no uso de **joins** para combinar informações de múltiplas tabelas, **funções agregadas** para cálculos estatísticos e **subqueries** para consultas mais eficientes. Também explorei a **normalização de dados**, entendendo como evitar redundâncias e melhorar a estrutura dos bancos de dados. Além disso, trabalhei com **otimização de consultas** usando índices, `GROUP BY`, `ORDER BY` e `HAVING`, garantindo que as buscas fossem feitas de maneira mais performática.  

---

### **Modelagem Relacional e Dimensional**  
Nesta Sprint, aprofundei meus conhecimentos sobre **modelagem relacional e dimensional**, compreendendo suas diferenças e aplicações.  

Na **modelagem relacional**, aprendi sobre a importância da **normalização**, garantindo que os dados sejam armazenados de forma eficiente e sem redundância. Trabalhei com **chaves primárias e estrangeiras**, assegurando a integridade referencial e evitando inconsistências. Compreendi como a **estruturação de tabelas em 1ª, 2ª e 3ª forma normal** ajuda a manter os bancos organizados, permitindo consultas mais eficazes.  

Na **modelagem dimensional**, explorei a diferença entre **bancos transacionais (OLTP)** e **bancos analíticos (OLAP)**, entendendo como cada um é estruturado para atender diferentes necessidades. Aprendi a **criar dimensões** e **tabelas fato**, aplicando o **modelo estrela** para otimizar a análise de dados.  

---

# Exercícios  

Os exercícios foram divididos em **Exercícios I** e **Exercícios II**, organizados nos arquivos SQL abaixo.  
Cada arquivo contém todas as queries com seus respectivos **enunciados comentados dentro do código**.

📌 **Exercícios I**  
👉 [Acessar Arquivo SQL](exercicios/exercicios_I.sql)  


📌 **Exercícios II - Exportação de Dados**   

Nesta etapa, foram geradas exportações de dados no formato **CSV**, seguindo os critérios estabelecidos no enunciado. A exportação foi feita através de consultas SQL no banco de dados, respeitando a estrutura das colunas exigidas e utilizando os delimitadores indicados.  

Os arquivos gerados foram disponibilizados no repositório e podem ser acessados nos links abaixo:  

📌 **Etapa 1 - Exportação dos 10 livros mais caros**  
- Formato: CSV  
- Separador: `,` (vírgula)  
- Colunas: `CodLivro`, `Titulo`, `CodAutor`, `NomeAutor`, `Valor`, `CodEditora`, `NomeEditora`  
👉 [Acessar Arquivo CSV](Exercicios/10_livros_mais_caros.csv)  

📌 **Etapa 2 - Exportação das 5 editoras com mais livros**  
- Formato: CSV  
- Separador: `|` (pipe)  
- Colunas: `CodEditora`, `NomeEditora`, `QuantidadeLivros`  
👉 [Acessar Arquivo CSV](Exercicios/5_editoras_mais_livros.csv)  

Os arquivos exportados foram gerados conforme as especificações e estão disponíveis para análise no repositório.  

---

# Evidências  

Abaixo estão as evidências da execução dos exercícios. Cada imagem contém o resultado obtido após rodar as queries no banco de dados. Os prints comprovam que os valores retornados estão corretos e alinhados com os enunciados.  

📌 **E01 - Listar todos os livros publicados após 2014**  
![Evidência E01](evidencias/Evidencias-Exercicios/E01.png)  

📌 **E02 - Listar os 10 livros mais caros**  
![Evidência E02](evidencias/Evidencias-Exercicios/E02.png)  

📌 **E03 - Listar as 5 editoras com mais livros na biblioteca**  
![Evidência E03](evidencias/Evidencias-Exercicios/E03.png)  

📌 **E04 - Quantidade de livros publicados por cada autor**  
![Evidência E04](evidencias/Evidencias-Exercicios/E04.png)  

📌 **E05 - Autores que publicaram fora da região Sul do Brasil**  
![Evidência E05](evidencias/Evidencias-Exercicios/E05.png)  

📌 **E06 - Autor com maior número de livros publicados**  
![Evidência E06](evidencias/Evidencias-Exercicios/E06.png)  

📌 **E07 - Autores sem nenhuma publicação**  
![Evidência E07](evidencias/Evidencias-Exercicios/E07.png)  

📌 **E08 - Vendedor com maior número de vendas concluídas**  
![Evidência E08](evidencias/Evidencias-Exercicios/E08.png)  

📌 **E09 - Produto mais vendido entre 2014-02-03 e 2018-02-02**  
![Evidência E09](evidencias/Evidencias-Exercicios/E09.png)  

📌 **E10 - Cálculo da comissão dos vendedores**  
![Evidência E10](evidencias/Evidencias-Exercicios/E10.png)  

📌 **E11 - Cliente com maior gasto na loja**  
![Evidência E11](evidencias/Evidencias-Exercicios/E11.png)  

📌 **E12 - Dependentes do vendedor com menor valor bruto de vendas**  
![Evidência E12](evidencias/Evidencias-Exercicios/E12.png)  

📌 **E13 - Os 10 produtos menos vendidos pelos canais E-Commerce ou Matriz**  
![Evidência E13](evidencias/Evidencias-Exercicios/E13.png)  

📌 **E14 - Gasto médio por estado da federação**  
![Evidência E14](evidencias/Evidencias-Exercicios/E14.png)  

📌 **E15 - Listar códigos das vendas deletadas**  
![Evidência E15](evidencias/Evidencias-Exercicios/E15.png)  

📌 **E16 - Quantidade média vendida de cada produto por estado**  
![Evidência E16](evidencias/Evidencias-Exercicios/E16.png)  

Essas evidências demonstram que as queries foram executadas corretamente e que os resultados correspondem ao esperado.  

---



# Certificados


