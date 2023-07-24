# import json

# with open('person.json', encoding= 'utf-8') as person:
#     dados = json.load(person)


# for chave, valor in dados.items():
#     print(chave, valor)

pessoas = open('person.json')
dados = pessoas.read()
pessoas.close()

print(pessoas)