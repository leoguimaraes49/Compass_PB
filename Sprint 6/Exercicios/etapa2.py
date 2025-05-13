# etapa2.py

def etapa2():
    # 1) Lista de 20 animais
    animais = [
        "gato", "cachorro", "papagaio", "elefante", "girafa",
        "tigre", "leão", "hipopótamo", "rato", "coelho",
        "panda", "urso", "zebra", "rinoceronte", "baleia",
        "golfinho", "canguru", "camelo", "cobra", "tartaruga"
    ]
    # 2) Ordena alfabeticamente
    animais.sort()
    # 3) Imprime um por linha
    print("Etapa 2 — animais ordenados:")
    for a in animais:
        print(a)
    # 4) Salva em arquivo
    with open("animais.txt", "w", encoding="utf-8") as f:
        for a in animais:
            f.write(a + "\n")
    print("\nArquivo 'animais.txt' criado com sucesso.")

if __name__ == "__main__":
    etapa2()
