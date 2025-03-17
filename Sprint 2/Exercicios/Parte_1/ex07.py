# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    print(conteudo, end='')

caminho = 'arquivo_texto.txt'
ler_arquivo(caminho)

