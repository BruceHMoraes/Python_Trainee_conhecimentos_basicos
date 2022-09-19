###Construa um algoritmo de votação para a Prefeitura Municipal de Volta
#Redonda. Os votos serão computados da seguinte maneira:
#-1 - sair
#0 - branco
#1 - Samuca
#2 - Neto
#3 - Baltazar
#>=4 - Nulo
#A saída deverá ser:
#+ O número do candidato vencedor
#+ O número de votos em branco
#+ O número de votos nulos
#+ o número de eleitores###

print('''informe em quem você deseja votar para a prefeitura de volta Redonda.
 digite 1 Samuca
        2  Neto
        3 Baltazar
        igual/maior que 4 nulo
        0 para branco
        -1 para sair
        digite aqui o numero: ''') 
neto = 0
baltazar = 0
samuca = 0
branco = 0
nulo = 0
l = []
while True:
    voto = int(input())
    if voto < 0:
        break
    if voto >=5:
        voto = 4
    l.append(voto)    
  
            
neto = l.count(2)
baltazar = l.count(3)
samuca = l.count(1)
branco = l.count(0)
nulo = l.count(4)


if neto > samuca and neto > baltazar:
    print("neto campeão das eleições")
elif samuca > neto and samuca > baltazar:
    print("samuca campeão das eleições")
elif baltazar > neto and baltazar > samuca:
    print("baltazar campeão das eleições") 
elif samuca == baltazar > neto:
    print("samuca e baltazar para o segundo turno")
elif samuca == neto > baltazar:
    print("samuca e neto para o segundo turno")   
elif baltazar == neto > samuca:
    print("Baltazar e neto para o segundo turno")   
elif baltazar == neto == samuca:
    print("Candidatos empatados todos para o segundo turno")         
    

print(f"votos em brancos {branco} e nulos {nulo}")

somavotos = neto + baltazar + samuca + branco + nulo
print(f"A somatoria dos votos é {somavotos}")
