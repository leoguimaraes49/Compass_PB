# A função calcula_saldo recebe uma lista de tuplas com lançamentos bancários e retorna o saldo final.
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0], lancamentos)
    return reduce(lambda saldo, valor: saldo + valor, valores, 0)


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))