import imdb
# Create an instance of the IMDb class
ia = imdb.IMDb()

# Retrieve a movie object
# Search for the movie by its title
movie_title = "Citizen Kane"  # Replace with your movie title
movies = ia.search_movie(movie_title)
movie = movies[0]
not_working_keys = ['directors', 'countries', 'writer', 'color info', 'original airdate']
working_keys = ['main', 'plot', 'awards', 'quotes', 'soundtrack', 'release dates']
# Update and retrieve specific information
ia.update(movie, working_keys)

for key in movie.keys():
    if (isinstance(movie[key], list)):
        itens = []
        for index, item in enumerate(movie[key]):
            if (index < 5550):
                itens.append(item)
            else:
                break
        if(key in ['cast', 'director', 'writer', 'producer', 'composer', 'cinematographer', 'editor']):
            formattedItens = ""
            formattedItensLength = 0
            for item in itens:
                if 'uncredited' not in item.currentRole and 'uncredited' not in item.notes and item.get('name') != None:
                    formattedItens += f"{item.get('name')}{f' as {item.currentRole}' if item.currentRole else ''}, "
                    formattedItensLength += 1
            
            print(f"{key} (first {formattedItensLength} of {len(itens)}): " + formattedItens)
        elif (key in ['make up', 'set decoration','casting director','editorial department','','','costume designer','special effects', 'music department', 'certificates', 'assistant director', 'production manager', 'sound crew', 'visual effects', 'akas', 'location management', 'costume department', 'stunt performer', 'visual effect', 'plot', 'synopsis', 'distributors', 'miscellaneous crew', 'art department', 'camera and electrical department', 'other companies', 'transportation department', 'script department']):
            pass
        elif (key in ['genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'languages']):
            print(f"{key} (first {len(itens)}): {itens}")















            
        else:
            print(f"{key} (first {len(itens)}): {itens}")
            pass
    elif (key in ['full-size cover url', 'smart long imdb canonical title', 'smart canonical title', 'long imdb canonical title', 'long imdb title', 'canonical title', 'imdbID', 'vote', 'localized title', 'cover url']):
        pass
    else:
        print(f"{key}: {movie[key]}")



    ##print(key)
    ##print(movie[key])
    ##if key == 'cast':
     ##   for item in movie[key]:
      ##      ##print(dir(item))
       ##     ##print(f"- {item['name']} as {item.currentRole} - {item.notes}")
        ##    break
