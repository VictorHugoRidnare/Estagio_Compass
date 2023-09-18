#Apresente a média da coluna contendo o número de filmes.

import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv', encoding='utf-8')
media = df['Number of Movies'].mean()
print(f'A média do número de filmes é {media}')