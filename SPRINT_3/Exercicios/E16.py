def soma_numeros(string):
    numeros = string.split(',')
    soma = sum(map(int, numeros))
    return soma

string_numeros = "1,3,4,6,10,76"
resultado = soma_numeros(string_numeros)

print(resultado)