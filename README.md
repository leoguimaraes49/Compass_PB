# Compass PB — Engenharia de Dados

Registro de exercícios e desafios desenvolvidos no programa de bolsas da Compass UOL, organizado em oito sprints. O repositório reúne práticas de SQL, Python, modelagem de dados, processamento em containers e serviços AWS.

## Desafio em destaque: dados de filmes

Nas sprints 5 a 8, o desafio explora um fluxo analítico sobre filmes e séries. Os arquivos e relatos documentam as seguintes etapas:

```text
CSVs locais + API TMDB
        ↓
Ingestão em S3 (camada Raw)
        ↓
Transformação com AWS Glue / PySpark (camada Trusted)
        ↓
Modelagem dimensional e dados em Parquet (camada Refined)
        ↓
Consultas com Athena e visualizações no QuickSight
```

O projeto inclui scripts de ingestão com Python e boto3, uma função Lambda para coleta de dados da API, jobs de transformação, dimensões e tabela de fatos. O recorte analítico documentado nas etapas finais aborda filmes do gênero guerra, incluindo métricas de produção, receita e retorno.

## Navegação pelas sprints

| Sprint | Conteúdo | Desafio |
| --- | --- | --- |
| [1](Sprint%201/README.md) | Consultas SQL e modelagem relacional e dimensional | [Modelagem de dados](Sprint%201/Desafio/README.md) |
| [2](Sprint%202/README.md) | Python, arquivos e ETL; análise exploratória | [Dados da Google Play Store](Sprint%202/Desafio/README.md) |
| [3](Sprint%203/README.md) | Python, Pandas, visualização e Docker | [Concert Tours](Sprint%203/Desafio/README.md) |
| [4](Sprint%204/README.md) | Exercícios com serviços AWS | [Análise de dados e S3](Sprint%204/Desafio/README.md) |
| [5](Sprint%205/README.md) | Ingestão de arquivos e dados de API | [Camada Raw de filmes e séries](Sprint%205/Desafio/README.md) |
| [6](Sprint%206/README.md) | AWS Glue e processamento de dados | [Camada Trusted](Sprint%206/Desafio/README.md) |
| [7](Sprint%207/README.md) | Modelagem e consultas analíticas | [Camada Refined](Sprint%207/Desafio/README.md) |
| [8](Sprint%208/README.md) | Visualização de dados no QuickSight | [Dashboard de filmes](Sprint%208/Desafio/README.md) |

## Tecnologias

- **Dados:** SQL, Python, Pandas, PySpark, CSV, JSON e Parquet.
- **Nuvem:** Amazon S3, AWS Lambda, AWS Glue, Amazon Athena e Amazon QuickSight.
- **Ambiente:** Docker e Docker Compose; boto3 e requests para integrações.

## Como explorar e executar

Clone o repositório e consulte o README da sprint ou do desafio desejado:

```bash
git clone https://github.com/leoguimaraes49/Compass_PB.git
cd Compass_PB
```

As atividades são independentes e não há um único comando para reproduzir todo o repositório. Os exemplos locais exigem as dependências indicadas em cada desafio; o desafio [Concert Tours](Sprint%203/Desafio/README.md), por exemplo, usa Docker Compose. As etapas na AWS dependem de conta, permissões, configuração dos serviços, dados de entrada e, quando aplicável, acesso à API TMDB; podem gerar custos.

Antes de executar, confira os caminhos e variáveis usados no código e adapte-os ao seu ambiente. Em particular, as instruções de execução da Sprint 5 devem ser confrontadas com `etapa-1/script.py`, pois há diferenças entre variáveis e caminhos documentados e os usados pelo script. Use credenciais temporárias fornecidas pelo ambiente ou por perfis AWS, sem incluí-las em arquivos versionados. Os resultados e evidências nas sprints registram as atividades originais; a reprodução integral depende desses recursos externos.

## Autor

Leonardo Guimarães Oliveira · [GitHub](https://github.com/leoguimaraes49) · [LinkedIn](https://www.linkedin.com/in/leo-guimaraes/)
