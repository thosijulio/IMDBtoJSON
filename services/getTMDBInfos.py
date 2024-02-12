import requests
import os
from dotenv import load_dotenv
import json

def getTMDBInfos(movie_title, movie_id):
    load_dotenv()

    # Replace 'YOUR_API_KEY' with your actual TMDb API key
    api_key = os.environ.get('TMDB_API_KEY')

    # TMDb API URL for searching movies
    search_by_movie_title_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}&language=pt-BR/credits"

    # Make the GET request to search for the movie
    response = requests.get(search_by_movie_title_url) if movie_title is not None else None


    if (response is not None and response.status_code == 200) or movie_id is not None:
        data = response.json() if movie_title else None

        # Check if there are results
        if data or movie_id is not None:
            # Assuming the first result is the desired movie if the movie_title arg
            movie_id = data['results'][0]['id'] if movie_title is not None else movie_id

            # Get details of the movie by its ID
            request_movie_enUS = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US&append_to_response=credits')
            request_movie_ptBR = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR&append_to_response=credits")

            if request_movie_ptBR.status_code == 200 and request_movie_enUS.status_code == 200:
                movie_details_ptBR = request_movie_ptBR.json()
                movie_details_enUS = request_movie_enUS.json()
                
                # Try to open the file, if exists
                try:
                    with open('movieInfo.json', 'r', encoding='utf-8') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    # If file doesnt exists, creats a new object
                    data = {}
                
                new_data = {
                    "title": {
                        "original": movie_details_enUS['original_title'],
                        "ptBR": movie_details_ptBR['title'],
                        "enUS": movie_details_enUS['title']
                    },
                    "releaseYear": movie_details_enUS['release_date'],
                    "genres": {
                        "ptBR": list(map(lambda genre: genre['name'], movie_details_ptBR['genres'])),
                        "enUS": list(map(lambda genre: genre['name'], movie_details_enUS['genres']))
                    },
                    "runtime": movie_details_enUS['runtime'],
                    "overview": {
                        "enUS": movie_details_enUS['overview'],
                        "ptBR": movie_details_ptBR['overview']
                    },
                    "tagline": {
                        "enUS": movie_details_enUS['tagline'],
                        "ptBR": movie_details_ptBR['tagline']
                    },
                    "productionCompanies": list(map(lambda company: { "name": company['name'], "countryCode": company['origin_country'] }, movie_details_enUS['production_companies']))
                }

                # write a JSON file with the new data (creating a new if is necessary)
                with open('movieInfo.json', 'w', encoding='utf-8') as file:
                    json.dump({ **data, **new_data}, file, indent=4, ensure_ascii=False)
            else:
                print("Failed to fetch movie details.")
        else:
            print("Movie not found.")
    else:
        print("Failed to perform the search.")
