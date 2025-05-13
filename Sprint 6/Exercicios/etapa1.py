
import random
def etapa1():
    # 1) Gera lista de 250 números aleatórios
    numeros = [random.randint(0, 1000) for _ in range(250)]
    # 2) Inverte a lista
    numeros.reverse()
    # 3) Imprime o resultado
    print("Etapa 1 — lista invertida:")
    print(numeros)

if __name__ == "__main__":
    etapa1()
