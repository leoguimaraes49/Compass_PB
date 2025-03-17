def funcao_csv():
    with open("estudantes.csv", mode="r", encoding="UTF-8") as arquivo:
        dados = list(map(lambda linha: linha.strip().split(","), arquivo))
        
        estudantes = list(
            map(lambda linha: (linha[0], sorted(map(int, linha[1:6]), reverse=True)), dados)
        )
        estudantes_ordenados = sorted(estudantes, key=lambda x: x[0])
        list(
            map(lambda estudante: print(
                f"Nome: {estudante[0]} Notas: {estudante[1][:3]} Média: {round(sum(estudante[1][:3]) / 3, 2)}"
            ), estudantes_ordenados)
        )

funcao_csv()