import os
from flask import Flask, render_template, url_for, flash, redirect
from Flask.forms import RegistrationForm, LoginForm
from BioFilmer.movies import get_movie_list

SECRET_KEY = os.getENV('SECRET_KEY_FLASK')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


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
    return render_template('movies.html',title='Movies', movies=moviess)


if __name__ == '__main__':
    app.run(debug=True)