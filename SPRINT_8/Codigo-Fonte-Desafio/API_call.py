import requests
import json
import boto3

def lambda_handler(event, context):
    
    api_key = 'minha-chave-api'
    actor_name = 'Jason Statham'
    
    # Criar URL de pesquisa para obter informações sobre o ator
    search_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={actor_name}'
    response = requests.get(search_url)
    actor_data = response.json()

    # Verifica se o ator foi encontrado nos resultados
    if 'results' in actor_data and len(actor_data['results']) > 0:
        actor_id = actor_data['results'][0]['id']

        # URL que obtém os créditos de filmes do ator
        filmes_url = f'https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={api_key}'
        response = requests.get(filmes_url)
        filmes_data = response.json()

        # Verifica se há informações de elenco de filmes disponíveis
        if 'cast' in filmes_data:
            all_movies = []
            for movie in filmes_data['cast']:
                movie_id = movie['id']
                movie_title = movie['title']

                # URL para obter detalhes do filme, incluindo orçamento e receita
                detalhes_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=budget,revenue'
                detalhes_response = requests.get(detalhes_url)
                details_data = detalhes_response.json()

                # Verifica se as informações de orçamento e receita estão disponíveis
                if 'budget' in details_data and 'revenue' in details_data:
                    budget = details_data['budget']
                    revenue = details_data['revenue']
                else:
                    budget = 'N/A'
                    revenue = 'N/A'

                # Adiciona informações do filme à lista de todos os filmes do ator
                all_movies.append({
                    'Título': movie_title,
                    'Data de Lançamento': movie['release_date'],
                    'Visão Geral': movie['overview'],
                    'Votos': movie['vote_count'],
                    'Média de votos': movie['vote_average'],
                    'Orçamento': budget,
                    'Receita': revenue
                })

            # Converte a lista de filmes em formato JSON
            json_data = json.dumps(all_movies, ensure_ascii=False, indent=4)

            # Conecta ao S3
            s3 = boto3.client('s3')
            bucket_nome = 'victor-data-lake-filmes'
            caminho_s3 = 'RAW/TMDB/JSON/2023-10-02/dados_do_ator.json'

            # Armazena os dados no S3
            s3.put_object(Bucket=bucket_nome, Key=caminho_s3, Body=json_data)

            print(f'Dados enviados para o S3 em {bucket_nome}/{caminho_s3}')
        else:
            print('Nenhum filme encontrado para o ator.')
    else:
        print('Ator não encontrado.')
