# Filtra produtos cujo valor unitário for superior à média e ordena pelo preço.
def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    return sorted(filter(lambda item: item[1] > media, conteudo.items()), key=lambda x: x[1])

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))
