# Importação do módulo random
import random

# Geração da lista aleatória
random_list = random.sample(range(500), 50)
random_list.sort()  # Ordenando a lista

# Cálculo das estatísticas
valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = round(sum(random_list) / len(random_list), 2)

# Cálculo da mediana
meio = len(random_list) // 2
if len(random_list) % 2 == 0:
    mediana = (random_list[meio - 1] + random_list[meio]) / 2
else:
    mediana = random_list[meio]

# Impressão no formato correto em uma única linha
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")