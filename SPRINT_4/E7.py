def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i

n = 10
pares_generator = pares_ate(n)
for num in pares_generator:
    print(num)