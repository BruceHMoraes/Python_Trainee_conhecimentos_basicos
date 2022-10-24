'''A soma das linhas de uma matriz 
e o seu valor total'''


notas = [
    [3, 5, 6],
    [4, 2, 9],
    [9, 7, 5],
    [1, 1, 1]
]

soma = 0
for linha in notas:
    print(linha)
    soma_linha = 0
    for coluna in linha:
        print(coluna)
        soma_linha = soma_linha + coluna
        soma = soma + coluna
    print(f'soma das linha é igual {soma_linha}')
print(f'total da matriz é {soma}')    

