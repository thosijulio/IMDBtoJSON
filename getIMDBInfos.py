from imdb import IMDb
import json
from utils.convertActorToDict import convert_actor_to_dict
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
parser.add_argument('--movie_id', type=int, help='Id from a movie in the IMDB API')
parser.add_argument('--movie_title', type=str, help='Title from a movie')

# Parse the command-line arguments
args = parser.parse_args()
movie_title = args.movie_title
movie_id = args.movie_id

# Create an instance of the IMDb class
ia = IMDb()

# Retrieve a movie object
# Search for the movie by its title

movies = ia.search_movie(movie_title) if movie_title is not None else None
movie = movies[0] if movies is not None else ia.get_movie(movie_id)

not_working_keys = ['directors', 'countries', 'writer', 'color info', 'original airdate']
working_keys = ['main', 'plot', 'awards', 'quotes', 'soundtrack', 'release dates']
# Update and retrieve specific information
ia.update(movie, working_keys)

 # Try to open the file, if exists
try:
    with open('movieTest.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    # If file doesnt exists, creats a new object
    data = {}
    pass


cast = [actor for actor in movie['cast'] if 'uncredited' not in str(actor.currentRole).lower() and 'uncredited' not in str(actor.notes).lower()]

serialized_cast = [convert_actor_to_dict(actor) for actor in cast]
    
new_data = {
    "cast": serialized_cast,
    "productionCountriesCodes": movie['country codes'],
    "colorInfo": movie['color info'],
    "languagesCodes": movie['language codes'],
    "IMDBRating": movie['rating'],
    "boxOffice": movie['box office']
}


for key in movie.keys():
    if (isinstance(movie[key], list)):
        itens = []
        for index, item in enumerate(movie[key]):
            if (index < 5550):
                itens.append(item)
            else:
                break
        if(key in ['director', 'writer', 'producer', 'composer', 'cinematographer', 'editor']):
            formattedItens = []
            
            new_data[key] = list(map(lambda people: { "name": people.get('name', ''), "notes": people.notes if people.notes != key else ''}, [people for people in movie[key] if 'uncredited' not in str(people.notes).lower()]))


# write a JSON file with the new data (creating a new if is necessary)
with open('movieTest.json', 'w', encoding='utf-8') as file:
    json.dump({ **data, **new_data}, file, indent=4, ensure_ascii=False)
