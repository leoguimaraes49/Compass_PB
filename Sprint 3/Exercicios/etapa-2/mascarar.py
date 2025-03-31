import hashlib

while True:
    texto = input("Digite um texto para mascarar (ou Ctrl+C para sair): ")
    hash_resultado = hashlib.sha1(texto.encode()).hexdigest()
    print(f"SHA-1: {hash_resultado}")

    