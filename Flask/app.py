import os
import pprint
from flask import Flask, render_template, url_for, flash, redirect, request
from BioFilmer.Flask.forms import RegistrationForm, LoginForm, FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from BioFilmer.movies import get_movie_list, match_movie
from BioFilmer.recommender import get_recommendations
from BioFilmer.database_handler import DatabaseHandler
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY



class MyForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])

movies_list = get_movie_list()
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/history', methods=['GET','POST'])
def add_to_history():
    if request.method == 'POST':
        title = request.form['name']
        rating = request.form['rating']
        #print("POSTing title: " + title + " with rating: " + rating)
        movie = match_movie(title, movies_list)
        movie['Rating'] = rating
        with DatabaseHandler("user1") as db:
            db.store(movie)
    return redirect(url_for('recommendations'))

@app.route('/movies', methods=['GET','POST'])
def movies():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Rating added for {form.name.data}!','success')
    return render_template('movies.html',title='Movies', movies=movies_list, form=form)

@app.route('/recommendations')
def recommendations():
    #TO-DO: for some reason the recommendations seem to always be the same. or maybe its me doing it wrong somehow
    final_recommendations = []
    with DatabaseHandler('user1') as handler:
        movies_seen = handler.read_all_rows()
        #pprint.pprint(movies_seen)
        recommended_movies_indexes = get_recommendations(movies_seen)[1]
        #from the movies list in theater, extract the indexes that match with the ones that the get recommendations returned
        for i in range(len(recommended_movies_indexes)):
            for j in range(len(movies_list)):
                if recommended_movies_indexes[i] == movies_list[j][0]:
                    final_recommendations.append(movies_list[j])
            # if movies_list[i][0] in recommended_movies[1]:
            #     final_recommendations.append(movies_list[i])
    return render_template('recommendations.html',title='Recommended',movies=final_recommendations)
if __name__ == '__main__':
    app.run(debug=True)
