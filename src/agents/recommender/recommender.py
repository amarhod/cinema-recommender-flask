import logging
import difflib
import pandas as pd
import numpy as np
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from recommender.utils import read_file, get_movie_list
from database_handler import DatabaseHandler


logging.basicConfig()
logging.root.setLevel(20)
logger = logging.getLogger(' Recommendation system agent ')


class Recommender():
    def __init__(self):
        logger.info('[Initialization] Starting agent')
        self.movies = get_movie_list()
        self.movies_seen = []
    
    def update_history(self):
        with DatabaseHandler("user1") as db:
            self.movies_seen = db.read_all_rows()

    def get_recommendations(self):
        self.update_history()
        df = read_file()
        movies_seen_indexes, movies_seen_title = [], []
        for movie in self.movies_seen:
            movies_seen_title.append(movie['Original_title'].strip())
            length = len(df.index)
            movie['Index']=length+1
            movies_seen_indexes.append(length+1)
            df = df.append(movie, ignore_index=True)
        df["Combined_words"] = df.apply(combine_columns, axis=1)
        cos_sim = find_similarity(df)
        rec1 = self.recommendations(df)
        recommended_movies = df[df.Index.isin(rec1)]
        return (recommended_movies, rec1)

    def recommendations(self, df):
        cos_sim = find_similarity(df)
        movies, indexes = [], []
        db = DatabaseHandler("user1")
        summed_score_series = pd.Series(0, dtype="float64")
        movies_seen_title = [movie['Original_title'].strip() for movie in self.movies_seen]
        for title in movies_seen_title:
            print(title)
            index = index_from_title(df,title)
            indexes += indexes_from_title(df,title)
            score_series = pd.Series(cos_sim[index-1])
            rating = db.get_rating(title)
            #print(f"{title} has rating: {rating}")
            if(rating == -1):
                score_series = score_series.apply(lambda x: 1-x)
            summed_score_series = summed_score_series.add(score_series, fill_value = 0) 
        db.close_connection()
        summed_score_series = summed_score_series.sort_values(ascending=False)
        top_indexes = list(summed_score_series.iloc[0:(10+len(indexes))].index)
        top_indexes_filtered = [n for n in top_indexes if n not in indexes]
        for i in top_indexes_filtered:
            #print(f'adding movie{(list(df.index)[i])}')
            movies.append(list(df.index)[i])
        return movies[0:10]

def combine_columns(row):
    try:
        return row['Original_title']+ " " + row['Genre'] + " " + row['Directors'] + " " + row['Actors'] + " " + row['Description']
    except Exception as e:
        print("Something went wrong")
        raise(e)

def title_from_index(df, index):
    return df[df.Index==index]["Original_title"].values[0]

def rating_from_index(df, index):
    return df[df.Index==index]["score"].values[0]

def index_from_title(df,title):
    indexes = df[df.Original_title==title.strip()]["Index"].values
    low = 10000 
    for ind in indexes:
        if ind < low:
            low = ind
    if low == 10000:
        low = None
    return low

def indexes_from_title(df,title):
    indexes = df[df.Original_title==title.strip()]["Index"].values.tolist()
    return indexes

def find_similarity(df):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['Combined_words'])
    cos_sim = cosine_similarity(count_matrix)
    return cos_sim

        


if __name__ == "__main__":
    movies_seen = [{'Actors': ' Lambert Wilson, Olga Kurylenko, Sidse Babett Knudsen, Riccardo '
            'Scamarcio, Eduardo Noriega',
  'Date': ' 17 jul 2020',
  'Description': 'Nio översättare har lyckats få ett riktigt drömjobb. '
                 'Tillsammans ska de översätta den avslutande delen av en '
                 'omåttligt populär fantasytrilogi. Hemlighetsmakeriet inför '
                 'boksläppet är på den nivån att de får utföra arbetet '
                 'isolerade i en lyxigt inredd bunker.',
  'Directors': ' Régis Roinsard',
  'Genre': 'Drama, Thriller',
  'Original_language': ' Engelska,  Franska ',
  'Original_title': ' Les traducteurs'},{'Actors': ' George Mackay, Dean-Charles Chapman, Richard Madden, Benedict '
            'Cumberbatch, Colin Firth, Mark Strong',
  'Date': ' 31 jan 2020',
  'Description': 'Två brittiska soldater får i uppdrag att ta sig långt in '
                 'bakom fiendelinjen för att varna ett regemente för ett '
                 'bakhåll som tyskarna planerar.',
  'Directors': ' Sam Mendes',
  'Genre': 'Drama, Krig',
  'Original_language': ' Engelska ',
  'Original_title': ' 1917'}]
    print(rec[0])
   # print(rec[1])
