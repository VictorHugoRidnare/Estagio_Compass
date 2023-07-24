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

def extrair_faturamento_por_ator(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()[1:]

    mapa_faturamento_ator = {}

    for linha in linhas:
        ator_dados =  linha.strip().split(',')
        ator_nome = ator_dados[0]
        faturamento_medio_por_filme = float(ator_dados[3])

        if ator_nome in mapa_faturamento_ator:
            mapa_faturamento_ator[ator_nome].append(faturamento_medio_por_filme)
        else:
            mapa_faturamento_ator[ator_nome] = [faturamento_medio_por_filme]    

    faturamento_medio_por_ator = {}
    
    for ator, faturamentos in mapa_faturamento_ator.items():
        faturamento_medio = sum(faturamentos) / len(faturamentos)
        faturamento_medio_por_ator[ator] = faturamento_medio
    
    return faturamento_medio_por_ator

def ator_com_maior_faturamento_medio(faturamendo_medio_por_ator):
    maior_faturamento_medio = 0
    ator_maior_faturamento = ""


    for ator, faturamento_medio in faturamendo_medio_por_ator.items():
        if faturamento_medio > maior_faturamento_medio:
            maior_faturamento_medio = faturamento_medio
            ator_maior_faturamento = ator

    return ator_maior_faturamento, maior_faturamento_medio        

nome_do_arquivo = "actors.csv"
ator, contagem_filmes = ator_com_mais_filmes(nome_do_arquivo)

print(f'O ator com mais filmes é: {ator}')
print(f'Número de filmes: {contagem_filmes}')

faturamento_por_ator = extrair_faturamento_por_ator(nome_do_arquivo)

print("FATURAMENTO MÉDIO POR ATOR: ")
for ator, faturamento_medio in faturamento_por_ator.items():
    print(f'{ator} U${faturamento_medio:.2f}')


faturamento_medio_por_ator = extrair_faturamento_por_ator(nome_do_arquivo)
ator_maior_faturamento, maior_faturamento_medio = ator_com_maior_faturamento_medio(faturamento_medio_por_ator)

print(f'O ator com maior média de faturamento por filme é {ator_maior_faturamento}')
print(f'Média de faturamento do ator por filme: U$ {maior_faturamento_medio:.2f}')