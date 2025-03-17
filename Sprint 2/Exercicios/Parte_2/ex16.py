# Crie uma classe Pessoa com um atributo privado e um público, utilizando properties.
class Pessoa:
    def __init__(self, id):
        self.__nome = ""  # Atributo privado
        self.id = id  # Atributo público
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
