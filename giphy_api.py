import requests
import random
import os
from dotenv import load_dotenv, find_dotenv


def get_random_gif():
    try:
        load_dotenv(find_dotenv())
        api_key = os.getenv('api_key')

        if not api_key:
            print("Отсутствует ключ API. Убедитесь, что он указан в файле .env.")
        else:
            search = input("GIF Search: ")

            offset = random.randint(0, 100)
            limit = 1

            url = f"https://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit={limit}&offset={offset}"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if "data" in data:
                    gif_data = data["data"]
                    if gif_data:
                        random_gif = gif_data[0]
                        if "images" in random_gif and "original" in random_gif["images"] and "url" in random_gif["images"]["original"]:
                            image_url = random_gif["images"]["original"]["url"]
                            print(f"Random Image URL: {image_url}")
                        else:
                            print("No image URL found for the random GIF.")
                    else:
                        print(f"No GIFs found for the search query: {search}")
                else:
                    print("Failed to fetch data from Giphy API.")
            else:
                print(f"Failed to fetch data from Giphy API. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
