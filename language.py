import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'YOUR_API_KEY' with your actual TMDb API key
api_key = os.environ.get('TMDB_API_KEY')

print(api_key)

# Movie title to search for
movie_title = "Matrix"  # Replace this with the movie title you're interested in

# TMDb API URL for searching movies
search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}&language=pt-BR/credits"

# Make the GET request to search for the movie
response = requests.get(search_url)

if response.status_code == 200:
    data = response.json()

    # Check if there are results
    if data['results']:
        # Assuming the first result is the desired movie
        movie_id = data['results'][0]['id']

        # Get details of the movie by its ID
        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR/credits"
        details_response = requests.get(movie_details_url)

        if details_response.status_code == 200:
            movie_details = details_response.json()
            # Get the Brazilian Portuguese title
            print(movie_details)
            # print(f"The title of the movie in Brazilian Portuguese is: {title_pt_br}")
        else:
            print("Failed to fetch movie details.")
    else:
        print("Movie not found.")
else:
    print("Failed to perform the search.")