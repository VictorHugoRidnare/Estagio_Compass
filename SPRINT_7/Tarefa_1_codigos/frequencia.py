#Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')

#calcula a contagem de cada filme
contagem_filmes = df['#1 Movie'].value_counts()

mais_frequentes = contagem_filmes.head(10)
rank = 0

for filme, contagem in mais_frequentes.items():
    rank += 1
    print(f'{rank}# - O filme {filme} aparece {contagem} vez(es) no dataset.')