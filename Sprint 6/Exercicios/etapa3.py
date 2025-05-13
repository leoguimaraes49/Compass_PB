import random
import time
import os
import names

# Passo 4: semente de aleatoriedade
random.seed(40)

# Passo 3: parâmetros
qtd_nomes_unicos     = 39_080
qtd_nomes_aleatorios = 1_000_000

# Preparar diretório de saída (usa os)
output_dir = "dataset_nomes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Passo 5.1: gerar lista de nomes únicos (aux)
start_time = time.time() 
aux = []
for _ in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())
print(f"{qtd_nomes_unicos} nomes únicos gerados.")

# Passo 5.2: gerar lista de nomes aleatórios (dados)
print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios…")
dados = []
for _ in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))
elapsed = time.time() - start_time
print(f"Geração concluída em {elapsed:.2f} segundos.")

# Passo 6: gravar um nome por linha em nomes_aleatorios.txt
output_file = os.path.join(output_dir, "nomes_aleatorios.txt")
with open(output_file, "w", encoding="utf-8") as f:
    for nome in dados:
        f.write(nome + "\n")

print(f"Arquivo '{output_file}' criado com {len(dados)} linhas.")
