import requests
import random


api_key = "rJFhFYNqDLsKALXUEIZMkdjJ2Wj3CoEs"
search = input("GIF Search: ")

offset = random.randint(0, 100)
limit = 1

url = f"https://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit={limit}&offset={offset}"

response = requests.get(url)
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
