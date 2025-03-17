# Implemente a função conta_vogais utilizando high order functions.
def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda c: c.lower() in "aeiou", texto)))

entrada = "Implementacao de High Order Functions"
print(conta_vogais(entrada))