# Dada as listas de nomes, sobrenomes e idades, imprima os dados na estrutura especificada.
Nomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(Nomes):
    print(f"{i} - {nome} {sobreNomes[i]} está com {idades[i]} anos")