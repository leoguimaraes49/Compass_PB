# ETL sobre o arquivo actors.csv seguindo as cinco etapas do exercício.
import os

def ler_arquivo_csv(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    cabecalho = linhas[0].strip().split(',')
    dados = []
    for linha in linhas[1:]:
        partes = linha.strip().split(',')
        if len(partes) >= 6:
            dados.append(partes[-6:])  
    
    return cabecalho, dados

def salvar_resultado(nome_arquivo, conteudo):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base_dir, nome_arquivo)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Etapa 1: Encontrar o ator/atriz com maior número de filmes
def etapa_1(dados):
    maior_ator = max(dados, key=lambda x: int(float(x[2].strip().replace(',', ''))))
    resultado = f"Nome: {maior_ator[0]} - Quantidade de filmes: {int(float(maior_ator[2].strip().replace(',', '')))}\n"
    salvar_resultado('etapa-1.txt', resultado)

# Etapa 2: Calcular a média da receita bruta de bilheteria dos filmes

def etapa_2(dados):
    valores = [float(x[5].strip().replace(',', '')) for x in dados if x[5].strip().replace(',', '').replace('.', '', 1).isdigit()]
    media = sum(valores) / len(valores)
    resultado = f"Média de receita bruta dos filmes: {round(media, 2)}\n"
    salvar_resultado('etapa-2.txt', resultado)

# Etapa 3: Ator/atriz com maior média de bilheteria por filme

def etapa_3(dados):
    maior_media = max(dados, key=lambda x: float(x[3].strip().replace(',', '')))
    resultado = f"Nome: {maior_media[0]} - Média por filme: {maior_media[3].strip()}\n"
    salvar_resultado('etapa-3.txt', resultado)

# Etapa 4: Contar ocorrências dos filmes com maior bilheteria
def etapa_4(dados):
    contagem_filmes = {}
    for linha in dados:
        filme = linha[4].strip()
        contagem_filmes[filme] = contagem_filmes.get(filme, 0) + 1
    
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))
    resultado = "\n".join([f"O filme {filme} aparece {quantidade} vez(es) no dataset" for filme, quantidade in filmes_ordenados])
    salvar_resultado('etapa-4.txt', resultado)

# Etapa 5: Ordenar atores pela receita total bruta
def etapa_5(dados):
    atores_ordenados = sorted(dados, key=lambda x: float(x[1].strip().replace(',', '')), reverse=True)
    resultado = "\n".join([f"{linha[0]} - ({linha[1].strip()})" for linha in atores_ordenados])
    salvar_resultado('etapa-5.txt', resultado)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base_dir, "actors.csv")
    cabecalho, dados = ler_arquivo_csv(caminho)
    etapa_1(dados)
    etapa_2(dados)
    etapa_3(dados)
    etapa_4(dados)
    etapa_5(dados)