def ler_numeros_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        return list(map(int, arquivo.readlines()))


lista_num = ler_numeros_arquivo("numeros.txt") 

numeros = ler_numeros_arquivo(lista_num)

numeros_pares = lambda x: x % 2 == 0

numeros_pares_filtrados = filter(numeros_pares, lista_num)

numeros_pares_ordenados = sorted(numeros_pares_filtrados, reverse=True)

cinco_maiores_pares = numeros_pares_ordenados[:5]

soma_cinco_maiores = sum(cinco_maiores_pares)

print("Lista dos 5 maiores números pares:", cinco_maiores_pares)
print("Soma dos 5 maiores números pares:", soma_cinco_maiores)