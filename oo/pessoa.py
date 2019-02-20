class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    wagner = Pessoa(nome='Wagner')
    herculano = Pessoa(wagner, nome='Herculano')
    print(Pessoa.cumprimentar(herculano))
    print(id(herculano))
    print(herculano.cumprimentar())
    print(herculano.nome)
    print(herculano.idade)
    for filho in herculano.filhos:
        print(filho.nome)
