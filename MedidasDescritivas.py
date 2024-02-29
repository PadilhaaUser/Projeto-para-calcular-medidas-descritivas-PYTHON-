import statistics

'''-------------------------------Começo do programa---------------------------------'''

lista = []

a = 1
while a != 0:
    a = float(input("\nDigite os valores desejados e depois digite 0 para finalizar: "))
    if a != 0:
        lista.append(a)

print("\nLista:",lista)

'''Parte 1
- cálculo da média'''
media = statistics.mean(lista)
print("\nMédia aritmética: ", media)

'''Parte 2 
- cálculo da mediana'''
mediana = statistics.median(lista)
print("\nMediana: ", mediana)

'''Parte 3
- cálculo da variância amostral'''
variancia = statistics.variance(lista)
print("\nVariância amostral: ", variancia)

'''Parte 4
- cálculo do desvio padrão'''
desvPad = statistics.stdev(lista)
print("\nDesvio padrão: ", desvPad)

'''Parte 5
- cálculo do coeficiente de variação'''
cv = desvPad/media * 100
print("\nCoeficiente de variação: ", round(cv,2), "%")

if cv > 30:
    print("-> O conjunto de dados é heterogêneo.\n")
else:
    print("-> O conjunto de dados é homogêneo.\n")

'''------------------------------------Fim do programa------------------------------------'''