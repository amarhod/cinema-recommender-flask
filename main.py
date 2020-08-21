from movies import get_movie_list
from start import ask_user
import pprint
from databasehandler import DatabaseHandler

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

def find_movie(user):
    pass


def main():
    print("Welcome!")
    user = input("Enter username: \n")
    with DatabaseHandler(f"{user}") as db:
        db.create_table(user)
        all_rows = db.read_all()
        #check if there is prior info on user
        if len(all_rows) > 0:
            find_movie(user)
            print("Passed!! Stage 2 is next")
        else:
            print("It seems this is your first time using this program.")
            first_time(user)
    

if __name__ == "__main__":
    #first_time()
    main()
    
