# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')

max_filmes = np.max(df['Number of Movies'])
ator_com_mais_filmes = df[df['Number of Movies'] == max_filmes]['Actor'].values[0]

print(f'O ator/atriz com maior número de filmes é {ator_com_mais_filmes} com {max_filmes} filmes.')