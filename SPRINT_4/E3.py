def calcular_valor_maximo(operadores, operandos):
    aplicar_operacao = lambda operador, operando: {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }[operador](operando[0], operando[1])
    
    resultados = map(aplicar_operacao, operadores, operandos)
    
    maior_valor = max(resultados)
    
    return maior_valor

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

for operador, operando in zip(operadores, operandos):
    print("Maior valor resultante:", operador, operando)