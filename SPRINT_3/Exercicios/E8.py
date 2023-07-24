list_A = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']


#A função recebe uma palavra como param. compara a palavra original com
#sua forma invertida através do slicing [::-1] e retorna a palavra de volta.

def palindromos(word):
    return word == word[:: -1]

palind_word = []

#o laço for irá percorrer cada palavra na list_A, chamando a função palindromos
#e passando cada palavra no índice de lista_A como argumento, e se a função
#retornar um palindromo, esta então, será adicionada à lista palind_word através
#do append usando a palavra que está sendo verificada no loop como argumento

for word in list_A:
    palindromos(word)
    if palindromos(word):
        print(f'A palavra: {word} é um palíndromo')
    else:
        print(f'A palavra: {word} não é um palíndromo')