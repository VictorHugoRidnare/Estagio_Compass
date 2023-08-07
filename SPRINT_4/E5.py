import csv

def funcao_media(notas):
    maiores_notas = sorted(notas, reverse= True)[:3]
    media = sum(maiores_notas)/3
    return round(media, 2)
    
    
with open("estudantes.csv", "r") as file:
    conteudo = csv.reader(file)
    for i in conteudo:
        nome = i[0]
        notas = list(map(int, i[1,6]))
        media = funcao_media(notas)
        print(f"Nome: {nome} Notas: {notas} Média: {media}")