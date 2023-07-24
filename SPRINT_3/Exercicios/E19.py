import random

lista_aleatoria = random.amostra(range(500), 50)

sorteada = sorted(lista_aleatoria)

valor_minimo = sorteada[0]

valor_maximo = sorteada[-1]

media = sum(sorteada) / len(sorteada)

n = len(sorteada)
if n % 2 == 0:
    mediana = (sorteada[n // 2 - 1] + sorteada[n // 2]) / 2
else:
    mediana = sorteada[n // 2]

print("Valor Mínimo:", valor_minimo)
print("Valor Máximo:", valor_maximo)
print("Valor Médio:", media)
print("Mediana:", mediana)
