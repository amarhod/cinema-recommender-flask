import os
import logging
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_classful import FlaskView, route
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from agents.recommender.utils import get_movie_list, match_movie
from agents.recommender.recommender import Recommender
from database.database_handler import DatabaseHandler


SECRET_KEY = os.urandom(32)
logging.basicConfig()
logging.root.setLevel(20)
logger = logging.getLogger(' Flask website agent ')
log = logging.getLogger('werkzeug')
log.disabled = True


class Website():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = SECRET_KEY
        logger.info('[Configuration] Configuring website agent')
        self.cinemaview = CinemaView()
        self.cinemaview.register(self.app, route_base='/')

    def start(self):
        logger.info('[Initialization] Starting agent')
        self.app.run(debug=True)
        

class MyForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])


class CinemaView(FlaskView):
    def index(self):
        return render_template('home.html', title='Home')

    def home(self):
        return render_template('home.html', title='Home')
    
    def movies(self):
        logger.info('[Communicating] Fetching movies from the Database')
        form = MyForm()
        if form.validate_on_submit():
            flash(f'Rating added for {form.name.data}!','success')
        return render_template('movies.html',title='Movies', movies=get_movie_list(), form=form)

    @route('/history', methods=['GET','POST'])
    def history(self):
        if request.method == 'POST':
            title = request.form['name']
            rating = request.form['rating']
            movie = match_movie(title, get_movie_list())
            movie['Rating'] = rating
            with DatabaseHandler("user1") as db:
                db.store(movie)
        return render_template('home.html', title='Home')

    def recommendations(self):
        final_recommendations = []
        recommender = Recommender()
        with DatabaseHandler('user1') as handler:
            recommended_movies_indexes = recommender.get_recommendations()[1]
            for i in range(len(recommended_movies_indexes)):
                for j in range(len(recommender.movies)):
                    if recommended_movies_indexes[i] == recommender.movies[j][0]:
                        final_recommendations.append(recommender.movies[j])
        return render_template('recommendations.html',title='Recommended',movies=final_recommendations)


if __name__ == '__main__':
    website = Website()
    website.start()
