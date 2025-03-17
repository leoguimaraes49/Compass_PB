# Retorna um generator para os valores pares no intervalo [2, n].
def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i

gen = pares_ate(10)
print(list(gen))