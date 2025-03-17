# Crie uma classe Calculo que contenha métodos de soma e subtração.
class Calculo:
    def somar(self, x, y):
        return x + y
    
    def subtrair(self, x, y):
        return x - y

# Testando a classe
x = 4
y = 5
calculo = Calculo()
print(f"Somando: {x}+{y} = {calculo.somar(x, y)}")
print(f"Subtraindo: {x}-{y} = {calculo.subtrair(x, y)}")
