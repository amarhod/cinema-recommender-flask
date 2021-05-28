import pandas as pd
from pathlib import Path
import os


#Finds the movie object for a given title
def match_movie(title, movies):
  movie_dict = {}
  for movie in movies:
    if movie[4].strip() == title.strip():
      movie_dict['Original_title'] = movie[4].strip()
      movie_dict['Original_language'] = movie[5]
      movie_dict['Genre'] = movie[3]
      movie_dict['Directors'] = movie[1]
      movie_dict['Actors'] = movie[2]
      movie_dict['Date'] = movie[6]
      movie_dict['Description'] = movie[7]
      return movie_dict
  return None

def read_file(filename='filmstaden.csv'):
    path = Path(os.path.abspath(os.getcwd()))
    new_path = path.parents[0].joinpath('agents/scraper/' + filename)
    df = pd.read_csv(new_path)
    df = df[['Index','Directors','Actors','Genre','Original_title','Original_language','Date','Description','Img_url']]
    df.fillna('') #fill in empty values cells
    df['Original_title'] = df['Original_title'].str.strip()
    return df

def get_movie_list():
  df = read_file()
  movie_list = df.values.tolist()
  for movie in movie_list:
    url = movie[-1]
    url_path = url.split('/')
    name = url_path[len(url_path)-1]
    movie[-1] = name
  return movie_list

if __name__ == '__main__':
  movies = get_movie_list()
  title = 'After we collided'
  movie = match_movie(title, movies)
  for (index, value) in enumerate(movie):
    print(index, value)
    print()
