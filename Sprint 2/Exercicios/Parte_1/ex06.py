# Implemente a função my_map que recebe uma lista e uma função, aplicando a função a cada elemento da lista.
def my_map(lista, f):
    return [f(x) for x in lista]
def potencia_de_2(x):
    return x ** 2

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(entrada, potencia_de_2)
print(resultado)
