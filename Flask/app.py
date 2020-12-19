import os
import pprint
from flask import Flask, render_template, url_for, flash, redirect
from BioFilmer.Flask.forms import RegistrationForm, LoginForm
from BioFilmer.movies import get_movie_list
from BioFilmer.recommender import get_recommendations
from BioFilmer.database_handler import DatabaseHandler
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

movies_list = get_movie_list()
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'user2' and form.password.data == 'user123':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Log in unsuccessful.','danger')
    return render_template('login.html',title='Log In', form=form)

@app.route('/account')
def account():
    return render_template('account.html', title='Account')

@app.route('/movies')
def movies():
    return render_template('movies.html',title='Movies', movies=movies_list)

@app.route('/recommendations')
def recommendations():
    #TO-DO: for some reason the recommendations seem to always be the same. or maybe its me doing it wrong somehow
    final_recommendations = []
    with DatabaseHandler('user1') as handler:
       # movies_seen = handler.read_all_rows()
        movies_seen = [{'Actors': ' Christian Bale, Michael Caine, Ken Watanabe, Liam Neeson, Katie '
                'Holmes, Gary Oldman, Rutger Hauer, Morgan Freeman',
      'Date': ' 24 jun 2020',
      'Description': 'Den ursprungliga berättelsen om hur Bruce Wayne bestämmer '
                     'sig för det goda och sitt alter ego Batman. Bruce Wayne ser '
                     'sina föräldrar mördas och vill hämnas på förövaren. Men - '
                     'han inser att hämnd inte löser något, utan blir i stället '
                     'Batman.',
      'Directors': ' Christopher Nolan',
      'Genre': 'Action, Äventyr',
      'Original_language': ' Engelska ',
      'Original_title': ' Batman Begins'}]
        pprint.pprint(movies_seen)
        recommended_movies = get_recommendations(movies_seen)
        #from the movies list in theater, extract the indexes that match with the ones that the get recommendations returned 
        for i in range(0,len(movies_list)):
            if movies_list[i][0] in recommended_movies[1]:
                final_recommendations.append(movies_list[i])
    return render_template('recommendations.html',title='Recommended',movies=final_recommendations)
if __name__ == '__main__':
    app.run(debug=True)
