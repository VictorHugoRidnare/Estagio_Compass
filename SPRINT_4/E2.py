def conta_vogais(texto):
    
    is_vogal = lambda char: char.lower() in 'aeiou'

    vogais_filtradas = filter(is_vogal, texto)

    quantidade_vogais = len(list(vogais_filtradas))

    return quantidade_vogais