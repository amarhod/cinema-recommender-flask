import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import difflib


def read_file(filename='250movies.csv'):
    df = pd.read_csv(filename)
    df = df[['Index','Title','Genre','Director','Actors','Plot']]
    #print(df.head())
    df.fillna('') #fill in empty values cells
    return df


def combine_columns(row):
    try:
        return row['Title']+ " " + row['Genre'] + " " + row['Director'] + " " + row['Actors'] + " " + row['Plot']
    except Exception as e:
        print("Something went wrong")
        raise(e) 


def title_from_index(df,index):
    return df[df.Index==index]["Title"].values[0]


def index_from_title(df,title):
    title_list = df['Title'].tolist()
    common = difflib.get_close_matches(title,title_list,1)
    titlesim = common[0]
    return df[df.Title ==titlesim]["Index"].values[0]

def find_similarity(df):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['Combined_words'])
    cos_sim = cosine_similarity(count_matrix)
    return cos_sim

def recommendations(title,df):
    cos_sim = find_similarity(df)
    movies = []
    index = index_from_title(df,title)
    score_series = pd.Series(cos_sim[index]).sort_values(ascending=False)
    top_ten_indexes  = list(score_series.iloc[1:11].index)
    for i in top_ten_indexes:
        movies.append(list(df.index)[i])
    return movies

def rec2(title,df):
    cos_sim = find_similarity(df)
    movies = []
    index = index_from_title(df,title)
    sim_movies = list(enumerate(cos_sim[index]))
    sim_movies_sorted = sorted(sim_movies,key=lambda x:x[1],reverse=True)
    return sim_movies_sorted

if __name__ == "__main__":
    df = read_file()
    df["Combined_words"] = df.apply(combine_columns,axis=1)
    #print(df)
    #print(title_from_index(df,2))
    #print(index_from_title(df,"The Lost Weekend"))
    cos_sim = find_similarity(df)
    rec1 = recommendations("Fargo",df)
    rec2 = rec2("Fargo",df)
    for rec in rec1:
        print(title_from_index(df,rec))
    for i in range(1,11):
        print(title_from_index(df,rec2[i][0])) 
    #print(recomended_movie_indexes)
    
    

