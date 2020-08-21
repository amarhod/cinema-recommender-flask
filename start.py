import pprint

def ask_user():
    print("We need some information about your taste")
    genres = ["Drama","Action","Skräck","Komedi","Sci-fi","Thriller"]
    user_rating = []
    for genre in genres:
        value = input(f"From 1-5 how much do you like {genre} movies: ")
        rating = int(value)
        if rating > 5:
            rating = 5
        user_rating.append({"Genre":genre,"Rating":rating})

    return sorted(user_rating, key=lambda i: i['Rating'],reverse=True) 


if __name__ == "__main__":
    print(ask_user())
 
