import requests
from config import OMDB_API_KEY


def search_movie(movie_name):

    url = "https://www.omdbapi.com/"

    parameters = {
        "apikey": OMDB_API_KEY,
        "t": movie_name
    }

    response = requests.get(url, params=parameters)

    return response.json()