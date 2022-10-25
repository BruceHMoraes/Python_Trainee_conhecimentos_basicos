
'''Construa um algoritmo capaz de calcular a quantidade de bichos que foram
premiado no ano durante os seis sorteios de cada mês e imprimi-los.'''


def somaLimpo(l):
 soma = []
 for i in l:
    soma.append(0)
 return soma

def contaMatriz(m, s, lista, mensagem):
 linha = len(m)
 coluna = len(m[0])
 for l in range(linha):
    for c in range(coluna):
        s[m[l][c]] = s[m[l][c]] + 1
 for i in range(len(lista)):
    print(lista[i], 'com', s[i], mensagem)

matriz = [[1,3,2,5,2,0],
          [3,4,1,2,1,4],
          [5,1,2,5,3,5],
          [4,2,4,3,4,1],
          [2,5,3,2,2,5],
          [0,0,0,0,0,0],
          [3,0,1,5,3,2],
          [2,3,2,2,5,1],
          [1,4,4,4,3,1],
          [0,1,5,1,5,2],
          [2,5,2,3,2,5],
          [3,3,3,3,3,3]]

bichos = ['vazio','porco','vaca','cachorro','gato','galo']
somatorio = somaLimpo(bichos)
contaMatriz(matriz,somatorio,bichos, 'prêmio')
print('-'*30)
