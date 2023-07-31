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

def contar_filmes_mais_frequentes(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()[1:] 

    filmes_frequencia = {}
    for linha in linhas:
        filme_data = linha.strip().split(',')
        filme_nome = filme_data[4]  

        if filme_nome in filmes_frequencia:
            filmes_frequencia[filme_nome] += 1
        else:
            filmes_frequencia[filme_nome] = 1

    filmes_mais_frequentes = {filme: frequencia for filme, frequencia in filmes_frequencia.items() if frequencia > 1}
    filmes_mais_frequentes = dict(sorted(filmes_mais_frequentes.items(), key=lambda item: item[1], reverse=True))

    return filmes_mais_frequentes

nome_do_arquivo = "actors.csv"
ator, contagem_filmes = ator_com_mais_filmes(nome_do_arquivo)
filmes_mais_frequentes = contar_filmes_mais_frequentes(nome_do_arquivo)

if not filmes_mais_frequentes:
    print("Não há filmes repetidos.")
else:
    print("Filmes mais frequentes e suas respectivas quantidades:")
    for filme, frequencia in filmes_mais_frequentes.items():
        print(f"{filme}: {frequencia} vezes")        


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