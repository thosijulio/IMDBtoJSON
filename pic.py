import requests
from bs4 import BeautifulSoup

def get_cast_picture(imdb_id):
    url = f'https://www.imdb.com/title/{imdb_id}/fullcredits/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cast_section = soup.find('table', class_='cast_list')
        
        if cast_section:
            cast_members = cast_section.find_all('img', class_='loadlate')
            print(cast_members)
            for img_tag in cast_members:
                
                if img_tag:
                    img_url = img_tag.get('loadlate')
                    actorName = img_tag.get('title')
                    print(f"Actor: {actorName}")
                    print(f"Image URL: {img_url}")
                else:
                    print("Image or name not found for a cast member.")
        else:
            print("Cast section not found on the page.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

# Replace 'tt0111161' with the IMDb ID of the movie you are interested in
get_cast_picture('tt0068646')