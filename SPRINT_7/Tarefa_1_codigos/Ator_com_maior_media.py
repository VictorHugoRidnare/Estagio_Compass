#Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv', encoding='utf-8')
indice_maximo = df['Average per Movie'].idxmax()
nome_max = df.at[indice_maximo, 'Actor']
media_max = df.at[indice_maximo, 'Average per Movie']

print(f'O ator com maior média por filme é {nome_max} com uma média de {media_max}')