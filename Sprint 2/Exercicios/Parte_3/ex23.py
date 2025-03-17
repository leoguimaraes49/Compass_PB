# A função calcular_valor_maximo recebe operadores e operandos, aplica operações e retorna o maior valor.
def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('-inf'),
        '%': lambda x, y: x % y if y != 0 else float('-inf')
    }
    
    resultados = list(map(lambda op_vals: operacoes[op_vals[0]](*op_vals[1]), zip(operadores, operandos)))
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]


print(calcular_valor_maximo(operadores, operandos))