from imdb import IMDb, Character
import json

def convert_to_dict(actor):
    name = actor.get('name', '') if hasattr(actor, 'get') else ''
    role = actor.currentRole if hasattr(actor, 'currentRole') and not isinstance(actor.currentRole, list) else ', '.join(map(str, getattr(actor, 'currentRole', [])))
    note = getattr(actor, 'notes', '')

    return {
        'name': name,
        'role': role if isinstance(role, str) else role.get('name', ''),
        'note': note
    }
# Create an instance of the IMDb class
ia = IMDb()

# Retrieve a movie object
# Search for the movie by its title
movie_title = "Kill Bill"  # Replace with your movie title
movies = ia.search_movie(movie_title)
movie = movies[0]
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

serialized_cast = [convert_to_dict(actor) for actor in cast]
    
new_data = {
    "cast": serialized_cast,
    "productionCountriesCodes": movie['country codes'],
    "colorInfo": movie['color info'],
    "languagesCodes": movie['language codes'],
    "IMDBRating": movie['rating'],
    "boxOffice": movie['box office']
}



for key in movie.keys():
    print(key)
    if (isinstance(movie[key], list)):
        print("\n")
        itens = []
        for index, item in enumerate(movie[key]):
            if (index < 5550):
                itens.append(item)
            else:
                break
        if(key in ['director', 'writer', 'producer', 'composer', 'cinematographer', 'editor']):
            formattedItens = []
            
            new_data[key] = list(map(lambda people: { "name": people.get('name', ''), "notes": people.notes if people.notes != key else ''}, movie[key]))
        ##elif (key in ['make up', 'set decoration','casting director','editorial department','','','costume designer','special effects', 'music department', 'certificates', 'assistant director', 'production manager', 'sound crew', 'visual effects', 'akas', 'location management', 'costume department', 'stunt performer', 'visual effect', 'plot', 'synopsis', 'distributors', 'miscellaneous crew', 'art department', 'camera and electrical department', 'other companies', 'transportation department', 'script department']):
          ##  pass
        elif (key in ['genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'languages']):
            pass
        else:
            pass
    elif (key in ['full-size cover url', 'smart long imdb canonical title', 'smart canonical title', 'long imdb canonical title', 'long imdb title', 'canonical title', 'imdbID', 'vote', 'localized title', 'cover url']):
        pass
    else:
        pass


 # write a JSON file with the new data (creating a new if is necessary)
with open('movieTest.json', 'w', encoding='utf-8') as file:
    json.dump({ **data, **new_data}, file, indent=4, ensure_ascii=False)
    ##print(key)
    ##print(movie[key])
    ##if key == 'cast':
     ##   for item in movie[key]:
      ##      ##print(dir(item))
       ##     ##print(f"- {item['name']} as {item.currentRole} - {item.notes}")
        ##    break
