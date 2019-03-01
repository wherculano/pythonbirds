class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    wagner = Homem(nome='Wagner')
    herculano = Pessoa(wagner, nome='Herculano')
    print(Pessoa.cumprimentar(herculano))
    print(id(herculano))
    print(herculano.cumprimentar())
    print(herculano.nome)
    print(herculano.idade)
    for filho in herculano.filhos:
        print(filho.nome)
    wagner.sobrenome = 'dos Santos'  # atributo de instancia
    del wagner.filhos
    herculano.olhos = 1
    del herculano.olhos  # Deleta atributo do objeto e não da classe
    print(wagner.__dict__)
    print(herculano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(herculano.olhos)
    print(wagner.olhos)
    print(id(Pessoa.olhos), id(wagner.olhos), id(herculano.olhos))
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(wagner, Pessoa))
    print(isinstance(wagner, Homem))
