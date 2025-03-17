# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
import json
def ler_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    print(dados)

caminho = 'person.json'
ler_json(caminho)