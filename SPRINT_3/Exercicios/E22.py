class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


if __name__ == "__main__":
    pessoa = Pessoa(0)
    pessoa.nome = 'Fulano De Tal'
    print(pessoa.nome)