# Instrução

Este arquivo será o relato da minha entrega. Neste documento, faço a organização geral ao longo da Sprint 7. Aqui são apresentadas as seções de aprendizado e a descrição detalhada do desafio realizado nesta etapa.

---

# Resumo

**Sprint 7 – Estruturação e Modelagem de Dados para Análise**: Nesta sprint, o foco foi:

* **Data Warehouse e Modelagem Multidimensional:** Aprendi sobre técnicas fundamentais para criar modelos dimensionais eficazes, incluindo a construção de tabelas fato e dimensões, abordando conceitos como star schema, snowflake schema e a importância das tabelas de fatos agregadas para análises rápidas e assertivas.
* **AWS AI para Programadores e DevOps:** Explorei como integrar o Amazon Q Developer em workflows de programação e DevOps, entendendo como aproveitar inteligência artificial da AWS para aumentar produtividade, aprimorar revisões de código e facilitar o desenvolvimento de software em ambientes cloud.

---

## Desafio de Filmes e Séries

Nesta sprint, realizei a **Entrega 4** do Desafio de Filmes e Séries, focando na criação da camada Refined com AWS Glue:

### Objetivo:

O objetivo foi praticar uma combinação dos conhecimentos adquiridos no programa, aplicando técnicas de modelagem dimensional e processamento de dados para criar uma camada de análise avançada (Refined).

### Entregáveis:

* Código em Python com AWS Glue detalhadamente comentado;
* Documentação com imagens explicativas de cada etapa executada;
* Modelo de dados multidimensional desenhado claramente para permitir insights e análises rápidas;
* Código-fonte em formato `.py`, implementando a criação da camada Refined.

### Descrição da Entrega:

Nesta etapa, construí a camada Refined do data lake, estruturando os dados provenientes da camada Trusted para facilitar consultas analíticas robustas e ágeis. Utilizando Apache Spark no AWS Glue, os dados foram transformados e organizados segundo um modelo dimensional bem estruturado, permitindo consultas eficientes em diferentes perspectivas analíticas.

Foram criadas tabelas e views automaticamente catalogadas pelo AWS Glue Data Catalog, garantindo fácil integração com ferramentas de visualização, como Amazon QuickSight. Todos os dados da camada Refined foram armazenados no formato Parquet particionado, seguindo boas práticas para otimização de desempenho.

[README do Desafio](Desafio/README.md)

---

## Conclusão

Nesta sprint, aprimorei:

* Conhecimentos em modelagem dimensional para Data Warehouse, entendendo melhor como estruturar dados para análises complexas e rápidas.
* A utilização prática de ferramentas AWS integradas à inteligência artificial, potencializando processos de desenvolvimento.
* Habilidades técnicas de processamento de dados escalável e eficiente com AWS Glue.


