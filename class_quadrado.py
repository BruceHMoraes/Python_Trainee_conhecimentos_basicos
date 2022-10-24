'''Classe Quadrado: Crie uma classe que modele um quadrado:
        a. Atributos: Tamanho do lado
        b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área'''

class quadrado:
    def __init__(self, lado):
        self.tamanho_lado = lado
    def mudar_valor_lado(self, lado):
        self.mudar_valor_lado = lado
    def retornar_valor_lado(self):
        return self.tamanho_lado
    def calcula_area(self):
        return self.tamanho_lado * self.tamanho_lado            
print('programa para calcular a área do quadrado')
valor = float(input('entre com o lado do quadrado:  '))
Quadrado = quadrado(valor)
q = Quadrado.calcula_area()
print(q)
