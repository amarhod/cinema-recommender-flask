from biose import get_movies
from tinydb import tinyDB, Query
movies_dict = get_movies()
db = tinyDB('movies.json')
