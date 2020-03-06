class Pessoa:
    def __init__(self, *filhos, nome = None, idade = None):
        self.filhos = list(filhos)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá ' + self.nome

if __name__ == '__main__':
    luciano = Pessoa(nome = 'Luciano')
    gilson = Pessoa(luciano, nome = 'Gilson')
    print(luciano.cumprimentar())
    print(gilson.cumprimentar())

    for filho in gilson.filhos:
        print(filho.nome)

