import requests
from bs4 import BeautifulSoup

def get_actor_photo(actor_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(actor_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing the actor's photo
        photo_element = soup.find('img', class_='s-lazy-image')

        if photo_element:
            # Extract the photo URL
            photo_url = photo_element.get('src')
            print(f"Actor Photo URL: {photo_url}")

            # Download the photo (optional)
            download_actor_photo(photo_url)
        else:
            print("Actor photo not found on the page.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

def download_actor_photo(photo_url):
    # You can implement code to download the photo here
    # For example, you can use the 'requests' library to download the image file
    pass

# Replace the URL with the IMDb actor's page you are interested in
actor_url = 'https://www.imdb.com/name/nm0000008/?ref_=ttfc_fc_cl_t1'
get_actor_photo(actor_url)