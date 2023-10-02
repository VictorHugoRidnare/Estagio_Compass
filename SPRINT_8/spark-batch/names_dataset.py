import random as rd
import time
import os
import names

#diretório onde o arquivo será salvo **colocar duas barras no diretorio ou r antes das aspas**
directory = 'C:\\Users\\Usuario\\Desktop\\EstagioCompassRepo\\SPRINT_8'

#nome do arquivo
file_name = "nomes_aleatorios.txt"

#caminhon completo do arquivo
full_path = os.path.join(directory, file_name)

if not os.path.exists(directory):
    os.makedirs(directory)

#gerar nomes aleatorios
rd.seed(40)
unique_names = 10000
random_names = 10000

aux = []

for i in range(0, unique_names):
    aux.append(names.get_full_name())

print('Gerando {} nomes aleatórios'.format(random_names))

with open(full_path, "w") as file:
    for _ in range(random_names):
        file.write(names.get_full_name() + "\n")
