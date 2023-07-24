class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y


if __name__ == "__main__":
    x = 4
    y = 5

    calculo = Calculo()

    resultado_soma = calculo.soma(x, y)
    print(f"Somando: {x}+{y} = {resultado_soma}")

    resultado_subtracao = calculo.subtracao(x, y)
    print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")
