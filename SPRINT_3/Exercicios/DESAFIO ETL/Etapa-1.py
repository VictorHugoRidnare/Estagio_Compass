def ator_com_mais_filmes(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()[1:]

    maximo_de_filmes = 0
    ator_com_mais_filmes = ""

    for linha in linhas:
        ator_dados = linha.strip().split(',')
        ator_nome = ator_dados[0]
        contagem_filmes = int(ator_dados[2])

        if contagem_filmes > maximo_de_filmes:
            maximo_de_filmes = contagem_filmes
            ator_com_mais_filmes = ator_nome

    return ator_com_mais_filmes, maximo_de_filmes

nome_do_arquivo = "actors.csv"
ator, contagem_filmes = ator_com_mais_filmes(nome_do_arquivo)

print(f'O ator com mais filmes é: {ator}')
print(f'Número de filmes: {contagem_filmes}')