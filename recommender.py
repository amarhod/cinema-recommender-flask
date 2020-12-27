import pandas as pd
import numpy as np
import difflib
from rake_nltk import Rake
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#OBS change the path to only 'filmstaden.csv' when running this script directly instead of running it from the app.py 
def read_file(filename='../filmstaden.csv'):
    df = pd.read_csv(filename)
    df = df[['Index','Directors','Actors','Genre','Original_title','Original_language','Date','Description','Img_url']]
    #print(df.head())
    df.fillna('') #fill in empty values cells
    return df

def combine_columns(row):
    try:
        return row['Original_title']+ " " + row['Genre'] + " " + row['Directors'] + " " + row['Actors'] + " " + row['Description']
    except Exception as e:
        print("Something went wrong")
        raise(e)

def title_from_index(df,index):
    return df[df.Index==index]["Original_title"].values[0]

def rating_from_index(df,index):
    return df[df.Index==index]["score"].values[0]

def index_from_title(df,title):
    title_list = df['Original_title'].tolist()
    common = difflib.get_close_matches(title,title_list,1)
    titlesim = common[0]
    return df[df.Original_title ==titlesim]["Index"].values[0]

def find_similarity(df):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['Combined_words'])
    cos_sim = cosine_similarity(count_matrix)
    return cos_sim

def recommendations(movies_watched ,df):
    cos_sim = find_similarity(df)
    movies = []
    indexes = []
    #Initialize an empty Series object to sum all the scores across several movies that the user has seen
    summed_score_series = pd.Series(0, dtype="float64")
    #TO-DO: Handle case if for some reason no movie is in the list
    for title in movies_watched:
        #Find index for the movie
        index = index_from_title(df,title)
        #Save all the indexes for the movies that the user has seen (used for filtering later)
        indexes.append(index)
        #Create a series of all the others titles and their similarity
        score_series = pd.Series(cos_sim[index-1])
        #Fetch user rating and invert the similarity values if the user did not like the movie
        # rating = rating_from_index(df,index)
        # if(rating == -1):
        #     score_series = score_series.apply(lambda x: 1-x)
        #Add the series to a summed series that aggregates the similarity scores for all movies prev. seen
        summed_score_series = summed_score_series.add(score_series, fill_value = 0) 
    #Sort the series with the most similar one at index 0 
    summed_score_series = summed_score_series.sort_values(ascending=False)
    #Create a list containing the indexes for the top movies.
    #If no top movie has been seen => 0-10. If one is seen already => 0-11
    #TO-DO:Handle if the dataframe containes less movies than we expect
    top_indexes = list(summed_score_series.iloc[0:(10+len(indexes))].index)
    #Remove index for movie already seen. Should result in a list length of 10
    top_indexes_filtered = [n for n in top_indexes if n not in indexes]
    for i in top_indexes_filtered:
        movies.append(list(df.index)[i])
    return movies[0:10]

#test method, disregard
def rec2(title,df):
    cos_sim = find_similarity(df)
    movies = []
    index = index_from_title(df,title)
    sim_movies = list(enumerate(cos_sim[index]))
    sim_movies_sorted = sorted(sim_movies,key=lambda x:x[1],reverse=True)
    return sim_movies_sorted

def dict_to_series(dictt):
    series = pd.Series(dictt, index = ["Original_title", "Original_language", "Genre", "Directors", "Actors", "Date", "Description"])
    return series

def get_recommendations(movies_seen):
    df = read_file()
    movies_seen_indexes = []
    movies_seen_title = []
    #Appends seen movies to the DataFrame which are needed for the rec1 func
    for movie in movies_seen:
        #Save the titles for all seen movies in an array (used as arg for rec1)
        movies_seen_title.append(movie['Original_title'].strip())
        #Save length of DataFrame so that the seen movies that get appended get the right Index
        length = len(df.index)
        #Add "Index" attribute to the movie dict so that the Indexing in df is correct
        movie['Index']=length+1
        movies_seen_indexes.append(length+1)
        df = df.append(movie, ignore_index=True)
        
    df["Combined_words"] = df.apply(combine_columns,axis=1)
    #print(df.head())
    #print(title_from_index(df,2))
    #print(index_from_title(df,"The Lost Weekend"))
    cos_sim = find_similarity(df)
    #movies_seen_title = ["Bad Boys for Life", "1917"]
    rec1 = recommendations(movies_seen_title,df)
    recommended_movies = df[df.Index.isin(rec1)]
    #print(recommended_movies)
    #rec2 = rec2("1917",df)
    #for rec in rec1:
        #print(rec)
        #print(title_from_index(df,rec))
    return (recommended_movies, rec1)

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
    rec = get_recommendations(movies_seen)
    print(rec[0])
   # print(rec[1])
