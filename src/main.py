from movies import get_movie_list
from start import ask_user
import pprint
from database_handler import DatabaseHandler
from recommender import get_recommendations

def first_time(user):
    user_rating = ask_user()
    movie_list = get_movie_list() #this part will need to be changed, i added a new class called movies.py so that i dont need to run the scraper everytime to get the movie info
    order_in_preference = []
    for item in user_rating:
        for movie in movie_list:
            if item['Genre'] in movie['Genre'] and movie not in order_in_preference:
                order_in_preference.append(movie)
    print("--------------------------------------------------------------")
    print("Based on your prefernces, we recommend that you watch one of the following movies:")
    limit = min(5,len(order_in_preference))
    for i in range (0,limit):
        print(f"{i+1}. " + order_in_preference[i]['Original_title'])

    watched = int(input(f"Which movie (1-{limit}) have you watched?\n"))
    while True:
       if watched < 1 or watched > limit:
          watched = int(input(f"Please select a number between 1 and {limit}:\n"))
       else:
          break

    print(f"Your selection ({order_in_preference[watched-1]['Original_title'].strip()}) has been saved!")
    with DatabaseHandler(user) as db:
        db.store(order_in_preference[watched-1])

def reorder_dict(dict):
    #CSV order : Directors, Actors, Genre, Original_title, Original_language, Date, Description
    #SQL order : Original_title, Original_language, Genre, Directors, Actors, Date, Description
    desired_order_list = [3, 4, 2, 0, 1, 5, 6]
    reordered_dict = {k: dict[k] for k in desired_order_list}
    return reordered_dict

#Calls "main" func in recommender.py with a list of dicts (containing each movie seen)
#Returns an array of indexes for top 10 movies recommended
#TO-DO: Return (from recommender.py) more than just index so that we can display the top 10 recommended list properly
def find_movie(movies_seen):
    movies = get_recommendations(movies_seen)
    print(movies)
    return movies


def main():
    print("Welcome!")
    user = input("Enter username: \n")
    with DatabaseHandler(f"{user}") as db:
        db.create_table(user)
        all_rows = db.read_all_rows()
        #check if there is prior info on user
        if len(all_rows) > 0:
            movies_recommended = find_movie(all_rows)
            print("Passed!! Stage 2 is next")
        else:
            print("It seems this is your first time using this program.")
            first_time(user)
    

if __name__ == "__main__":
    #first_time()
    main()
    
