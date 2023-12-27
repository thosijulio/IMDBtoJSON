import imdb
# Create an instance of the IMDb class
ia = imdb.IMDb()

# Retrieve a movie object
# Search for the movie by its title
movie_title = "Catch me if you can"  # Replace with your movie title
movies = ia.search_movie(movie_title)
movie = movies[0]
not_working_keys = ['directors', 'countries', 'writer', 'color info', 'original airdate', 'plot', 'awards', 'quotes', 'soundtrack', 'release dates']
working_keys = ["main"]
# Update and retrieve specific information
ia.update(movie, working_keys)

#print(movie['title'])
#print(movie.get('awards'))
#print(movie.get('quotes'))
#print(movie.get('genres'))
#print(movie.get('directors'))  # Check for directors key
#print(movie.get('writers'))
#print(movie.get('original airdate'))      
#print(movie.get('color info'))      
#print(movie.get('countries')) 
#print(movie.get('writers')) 
#print(movie.get('soundtrack')) 
#print(movie.get('release dates'))
#print(movie.get('original air date'))
#print(movie.keys())

for key in movie.keys():
    ##print(key + ':')
    if key == 'language codes':
        for language in movie[key]:
            print(language)
    if key == 'cast':
        for item in movie[key]:
            ##print(dir(item))
            ##print(f"- {item['name']} as {item.currentRole} - {item.notes}")
            break
    