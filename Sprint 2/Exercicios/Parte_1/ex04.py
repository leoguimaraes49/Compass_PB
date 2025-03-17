# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
def remover_duplicatas(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remover_duplicatas(lista_teste)
print(resultado)
