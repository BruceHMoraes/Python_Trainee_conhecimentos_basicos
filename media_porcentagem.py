notas = [[ 6.0, 7.0, 7.5, 8.0,10.0],
 [ 9.0, 8.0, 7.0, 8.0, 8.0],
 [ 5.0, 7.5, 8.0, 8.0, 7.0],
 [ 5.0, 6.0, 8.0, 8.0, 7.0],
 [ 6.0,10.0,10.0, 9.0, 7.0],
 [ 8.0, 9.0, 9.5, 7.5, 9.0]]

linha = len(notas)
coluna = len(notas[0])
caixa = []
for i in range(linha):
 s = 0
 for j in range(coluna):
    s = s + notas[i][j]
 caixa.append(s/coluna)
print(caixa)
totalMedias = 0
for i in range(len(caixa)):
 totalMedias += caixa[i]
print(totalMedias)
porcentagens = []
for i in caixa:
 porcentagens.append(i/totalMedias)
for i in range(len(caixa)):
 print(i+1, caixa[i], '%.2f' % (porcentagens[i]*100))
print(f"O total das médias são: {totalMedias}")
