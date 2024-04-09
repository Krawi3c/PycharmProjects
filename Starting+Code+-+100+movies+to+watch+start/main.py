import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL).text

page = BeautifulSoup(response, "html.parser")

all_movies = page.find_all("h3", class_='title')
movies = [movie.text for movie in all_movies]
movies.reverse()

with open('movies.txt', 'w', encoding="utf-8") as file:
   file.write("\n".join(str(item) for item in movies))
