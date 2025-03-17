# Escreva uma função que recebe uma string de números separados por vírgula e retorna a soma de todos eles.
def soma_numeros(string_numeros):
    return sum(map(int, string_numeros.split(',')))

# Testando a função
entrada = "1,3,4,6,10,76"
resultado = soma_numeros(entrada)
print(resultado)