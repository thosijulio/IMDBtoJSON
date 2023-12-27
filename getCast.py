import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Search for the movie by its title
movie_title = "The Godfather"  # Replace with your movie title
movies = ia.search_movie(movie_title)

if movies:
    # Assuming the first movie in the search result is the correct one
    movie = movies[0]
    movie_id = movie.movieID

    # Fetch the movie details including the cast
    ia.update(movie, ['main', 'plot', 'awards', 'quotes', 'full credits', 'directors', 'countries', 'writer', 'color info', 'original airdate', 'genres'])


    # Get the cast (actors) of the movie 
    cast = movie.get('cast')
    awards = movie.get('awards')

    print(awards)

#    if not cast:
#        print(f"Actors in '{movie_title}':")
#        for actor in cast:
#            print(f"- {actor['name']} as {actor.currentRole}")
#    else:
#        print("No cast information available for this movie.")
#else:
#    print("Movie not found.")