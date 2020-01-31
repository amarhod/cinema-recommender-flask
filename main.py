from biose import get_movies
from tinydb import TinyDB, Query


movies_dict = get_movies()
db = TinyDB('movies.json')
db.insert_multiple(movies_dict)
