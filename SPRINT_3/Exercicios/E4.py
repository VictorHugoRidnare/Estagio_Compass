# Primeiro se cria a função que irá verificar se um número é primo ou não
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Depois criamos uma lista para armazenas os numeros primos

primos = []

# Por fim, utilizamos um laço para percorrer os numeros de 1 a 100 e chamando
# a função is_prime passando num como parâmetro para a verificação que será
# feita pela função.

for num in range(1, 101):
    if is_prime(num):
        primos.append(num)


print(primos) #para imprimir a lista inteira

for i in primos: #para imprimir os items um por um
    print(i)