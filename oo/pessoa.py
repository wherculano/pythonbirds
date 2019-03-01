class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    wagner = Mutante(nome='Wagner')
    herculano = Homem(wagner, nome='Herculano')
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
    print(Pessoa.olhos)
    print(herculano.olhos)
    print(wagner.olhos)
    print(id(Pessoa.olhos), id(wagner.olhos), id(herculano.olhos))
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(wagner, Pessoa))
    print(isinstance(wagner, Homem))
    print(wagner.olhos)
    print(wagner.cumprimentar())
    print(herculano.cumprimentar())