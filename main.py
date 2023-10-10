from bs4 import BeautifulSoup

import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
movie_titles = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# movies = [movie.getText() for movie in movie_titles]
# for n in range(len(movies) - 1, -1, -1):
#     print(movies[n])
reverse_movie_titles = movie_titles[::-1]
# print(reverse_movie_titles)
with open("top_100_movies.txt", "w") as data:
    for movie_title in reverse_movie_titles:
        # print(movie_title.getText())
        data.write(movie_title.getText()+"\n")

