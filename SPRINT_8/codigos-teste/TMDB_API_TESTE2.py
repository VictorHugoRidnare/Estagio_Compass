import requests
import pandas as pd
from IPython.display import display

api_key = 'chave-api'
url = f'https://api.themoviedb.org/3/person/976-jason-statham?api_key={api_key}language=pt-BR'

response = requests.get(url)
actor_data = response.json()

jStatham_movies = f'https://api.themoviedb.org/3/person/976-jason-statham/movie_credits?api_key={api_key}'
response = requests.get(jStatham_movies)
movies_data = response.json()

if 'cast' in movies_data:
    movies = []
    for movie in movies_data['cast']:
        movies.append({

                'Título': movie['title'],
                'Data de lançamento': movie['release_date'],
                'Avaliações': movie['vote_average']
        })
    
    df = pd.DataFrame(movies)  

    print(df)
else:
    print("Não encontrado")  

print(actor_data)            
print(movies_data)            