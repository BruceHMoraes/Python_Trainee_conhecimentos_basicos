#Construa um algoritmo capaz de permitir a entrada, via teclado, do nome
#do aluno e suas duas notas até que o nome sair aparecer e terminar o
#programa. No final deverá apresentar o nome e a média das notas junto com
#mensagem aprovado (>=7) ou reprovado (<7).

lista = []
while True:
    nome = input('Entre com o nome: ')
    if nome.lower() == 'sair':
        break
    lst = []
    while True:
        n = float(input('Entre com nota: '))
        if n == -1:
            break
        lst.append(n)
    registro = (nome, lst)
    lista.append(registro)
for i in lista:
    print(i[0])
    soma = 0
for j in i[1]:
    soma = soma + j
    print(soma/len(i[1]))
for i in lista:
    media = (i[1]+i[2])/2
    if media >= 7:
        print('aluno: ', i[0], 'média: ', media, 'aprovado')
    else:
        print('aluno: ', i[0], 'média: ', media, 'reprovado')
