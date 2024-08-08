import time
import logging
import requests
import random
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram import executor

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)

api_key = os.getenv('api_key')
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
user_search_queries = {}


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name} {time.asctime()}')
    user_search_queries[user_id] = ""
    await message.reply(f"Hello, {user_full_name}! Write a word or emoji to get a GIF on this topic.")


@dp.message_handler(lambda message: True)
async def search_gif_handler(message: types.Message):
    user_id = message.from_user.id
    search = message.text

    if search:
        offset = random.randint(0, 100)
        limit = 1

        url = f"https://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit={limit}&offset={offset}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if "data" in data:
                gif_data = data["data"]
                if gif_data:
                    random_gif = gif_data[0]
                    if "images" in random_gif and "original" in random_gif["images"] and "url" in random_gif["images"]["original"]:
                        gif_url = random_gif["images"]["original"]["url"]
                        await message.reply_document(gif_url)
                    else:
                        await message.reply("Не удалось найти URL изображения для случайного GIF.")
                else:
                    await message.reply(f"Нет GIF-изображений для запроса: {search}")
            else:
                await message.reply("Не удалось получить данные из API Giphy.")
        except Exception as e:
            await message.reply(f"Произошла ошибка при запросе GIF: {str(e)}")

    user_search_queries[user_id] = ""


if __name__ == '__main__':
    executor.start_polling(dp)
