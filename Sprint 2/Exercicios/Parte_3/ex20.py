# Leia um arquivo contendo 10.000 números inteiros e exiba os 5 maiores pares e sua soma.
def processar_numeros(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        numeros = list(map(int, f.readlines()))
    
    maiores_pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)[:5]
    soma_maiores_pares = sum(maiores_pares)
    
    print(maiores_pares)
    print(soma_maiores_pares)

processar_numeros('number.txt')