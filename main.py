import imdb
import xml.etree.ElementTree as ET

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Fetch movie data by its title
movie_title = "Chicken Run: Dawn of the Nugget"
movies = ia.search_movie(movie_title)
if movies:
    # Get the first movie (assuming it's the correct one)
    movie = movies[0]
    ia.update(movie)

    # Create an XML structure
    movie_xml = ET.Element('movie')
    ET.SubElement(movie_xml, 'title').text = movie['title']

    imdb_info = ET.SubElement(movie_xml, 'imdb')
    ET.SubElement(imdb_info, 'id').text = movie.movieID
    ET.SubElement(imdb_info, 'rating').text = str(movie.get('rating', 'N/A'))
    ET.SubElement(imdb_info, 'votes').text = str(movie.get('votes', 'N/A'))
    ET.SubElement(imdb_info, 'url').text = f"https://www.imdb.com/title/{movie.movieID}/"

    # Add other necessary movie info to the XML structure
    # For example, cast, director, writers, genres, etc.

    # Create the XML file
    xml_file = ET.ElementTree(movie_xml)
    xml_file.write('movie_data.xml', encoding='utf-8', xml_declaration=True)
else:
    print("Movie not found")