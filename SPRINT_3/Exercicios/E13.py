lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def potencia(numero):
    return numero ** 2

def my_map(listas, funcao):
    resultado = []
    for indice in listas:
        resultado.append(funcao(indice))
    return resultado    

nova_lista = (my_map(lista, potencia))

print(nova_lista)