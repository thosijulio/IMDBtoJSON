import argparse
from services.getIMDBInfos import getIMDBInfos
from services.getTMDBInfos import getTMDBInfos

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()
    parser.add_argument('--imdb_movie_id', type=int, help='Id from a movie in the IMDB API')
    parser.add_argument('--tmdb_movie_id', type=int, help='Id from a movie in the TMDB API')
    parser.add_argument('--movie_title', type=str, help='Title from a movie')

    # Parse the command-line arguments
    args = parser.parse_args()
    movie_title = args.movie_title
    imdb_movie_id = args.imdb_movie_id
    tmdb_movie_id = args.tmdb_movie_id

    getTMDBInfos(movie_title, tmdb_movie_id)
    getIMDBInfos(movie_title, imdb_movie_id)

if __name__ == '__main__':
    main()

