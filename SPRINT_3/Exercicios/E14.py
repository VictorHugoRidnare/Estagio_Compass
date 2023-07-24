def parametros(*args, **kwargs):
    for arg in args:
        print(arg, end='\n')

    for value in kwargs.values():
        print(f'{value}')

parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)