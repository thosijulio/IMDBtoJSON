import imdb
import json

def serialize_character(character):
    return {
        'name': character.get('name', ''),
        'role': getattr(character, 'currentRole', ''),
        'note': getattr(character, 'notes', '')
    }

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Retrieve a movie object
# Search for the movie by its title
movie_title = "Inglorious Bastard"  # Replace with your movie title
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
serialized_cast = [serialize_character(actor) for actor in cast]
    
new_data = {
    "cast": serialized_cast
}

 # write a JSON file with the new data (creating a new if is necessary)
with open('movieTest.json', 'w', encoding='utf-8') as file:
    json.dump({ **data, **new_data}, file, indent=4, ensure_ascii=False)

for key in movie.keys():
    if (isinstance(movie[key], list)):
        print("\n")
        itens = []
        for index, item in enumerate(movie[key]):
            if (index < 5550):
                itens.append(item)
            else:
                break
        if(key in ['cast', 'director', 'writer', 'producer', 'composer', 'cinematographer', 'editor']):
            formattedItens = []
            for item in itens:
                if 'uncredited' not in item.currentRole and 'uncredited' not in item.notes and item.get('name') != None:
                    if key == 'cast' and isinstance(item.currentRole, list):
                        character_role = str(item.currentRole)
                        character_name = character_role.split('_')[-2] if '_' in character_role else character_role
                        formattedItens.append({ 'name': item.get('name'), 'role': character_name, 'notes': item.notes })
                    elif key == 'cast':
                        character_role = str(item.currentRole)
                        character_name = character_role.split('_')[-2] if '_' in character_role else character_role
                        formattedItens.append({ 'name': item.get('name'), 'role': character_name, 'notes': item.notes })
                    else:
                        formattedItens.append({ 'name': item.get('name'), 'notes': item.notes })
                    # f"{item.get('name')}{f' as {item.currentRole}' if item.currentRole else f' as {item.notes}' if item.notes and item.notes != key else ''}, \n"
            
            print(f"{key}: {formattedItens}")
        ##elif (key in ['make up', 'set decoration','casting director','editorial department','','','costume designer','special effects', 'music department', 'certificates', 'assistant director', 'production manager', 'sound crew', 'visual effects', 'akas', 'location management', 'costume department', 'stunt performer', 'visual effect', 'plot', 'synopsis', 'distributors', 'miscellaneous crew', 'art department', 'camera and electrical department', 'other companies', 'transportation department', 'script department']):
          ##  pass
        elif (key in ['genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'languages']):
            print(f"{key} (first {len(itens)}): {itens} \n")
            
        else:
            print(f"{key} ({len(itens)}): {itens}")
            pass
    elif (key in ['full-size cover url', 'smart long imdb canonical title', 'smart canonical title', 'long imdb canonical title', 'long imdb title', 'canonical title', 'imdbID', 'vote', 'localized title', 'cover url']):
        pass
    else:
        pass



    ##print(key)
    ##print(movie[key])
    ##if key == 'cast':
     ##   for item in movie[key]:
      ##      ##print(dir(item))
       ##     ##print(f"- {item['name']} as {item.currentRole} - {item.notes}")
        ##    break
