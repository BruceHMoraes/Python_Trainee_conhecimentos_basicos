'''Criar um algoritmo capaz de calcular o faturamento de uma lista de
produtos com suas respectivas quantidades e preço.
Verifique a entrada dos produtos, ao digitar sair a captação se encerra.
Calcular o faturamento com a equação:
faturamento = faturamento + (quantidade * preço)
Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis
quantidade e preço.'''

quantidade = 0
preço = 0
faturamento = 0

lista = []
while True:
    produto = str(input('informe o produto:  '))
    if produto.lower() == 'sair':
        break
    quantidade = int(input('informe a quantidade:  '))
    preço = float(input('informe o preço: '))
    lista.append((produto, quantidade, preço))
    
for i in lista:
    faturamento = faturamento + (i[1] * i[2]) 
print(f'O seu faturamento é:  {faturamento :.2f}')    
