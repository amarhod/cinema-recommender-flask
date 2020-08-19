from movies import get_movie_list
from start import ask_user
import pprint

def first_time():
    user_rating = ask_user()
    movie_list = get_movie_list() #this part will need to be changed, i added a new class called movies.py so that i dont need to run the scraper everytime to get the movie info
    order_in_preference = []
    for item in user_rating:
        for movie in movie_list:
            if item['Genre'] in movie['Genre'] and movie not in order_in_preference:
                order_in_preference.append(movie)
    print("--------------------------------------------------------------")
    print("Based on your prefernces, we recommend that you watch one of the following movies:")
    for i in range (0,5):
        print(order_in_preference[i]['Original_title'])
    



if __name__ == "__main__":
    first_time()
    
