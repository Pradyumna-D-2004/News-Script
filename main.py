import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('KEY')


url = (f'https://newsapi.org/v2/top-headlines?country=us&apiKey={key}')

response = requests.get(url).json()

newsIndex = random.randint(0, 10)


newsTitle = response['articles'][newsIndex]['title']
newsDesc = response['articles'][newsIndex]['description']

newsUrl = response['articles'][newsIndex]['url']

os.system('cls')

print("PY NEWS!")
print(f"{newsTitle}\n")
print(newsDesc)

print(f"\nSource: {newsUrl}\n")
