from bs4 import BeautifulSoup
import requests

# read the 100 greatest movies from Empireonline.com and output the movies to a txt file
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, 'html.parser')

movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = []

for movie in movies:
    movie_titles.insert(0, movie.getText())

with open("100 greatest movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")
