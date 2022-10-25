class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def emagrecer(self, peso):
        self.peso -= peso

    def engordar(self, peso):
        self.peso += peso

    def envelhecer(self):
        self.idade += 1 # a quantidade de numeros que você adicionar, será a quantidade de anos que ira envelhecer.
        if self.idade < 21:
            self.crescer(0.005)
    def crescer(self, altura):
        self.altura += altura
pessoa = Pessoa('Bruce', 30, 97.8, 1.80)
pessoa.engordar(3)
pessoa.envelhecer()
pessoa.crescer(1.0)
print(pessoa.peso, pessoa.altura, pessoa.nome, pessoa.idade )


