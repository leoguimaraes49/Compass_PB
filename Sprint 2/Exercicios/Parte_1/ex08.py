# Escreva uma função que recebe um número variável de parâmetros não nomeados e nomeados e imprime seus valores.
def imprimir_valores(*args, **kwargs):
    for valor in args:
        print(valor)
    for valor in kwargs.values():
        print(valor)                                  
imprimir_valores(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
