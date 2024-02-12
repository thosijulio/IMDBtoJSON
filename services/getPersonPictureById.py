import requests
from bs4 import BeautifulSoup

def getPersonPictureById(actorId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(f'https://www.imdb.com/name/nm{actorId}', headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing the actor's photo
        photo_element = soup.find('img', class_='ipc-image')

        if photo_element:
            # Extract the photo URL
            photo_url = photo_element.get('src')
            if photo_url:                
                return photo_url.split('._')[0] + '.jpg'
            else:
                return ''
        else:
            print("Actor photo not found on the page.")
            return ""
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return ""
