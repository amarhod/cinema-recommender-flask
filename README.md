## Cinema recommender

A cinema recommender implemented in Flask.
By scraping current movies on cinema (Filmstaden), the user gets recommendations based on similarity score with prior watched movies.

## Code functionality 
- **scraper** - Scrapes Filmstaden for current movies and stores movie information in a .csv file as well as storing the movie posters locally.
- **recommender** - Based on previously seen movies and the rating by the user, finds current movies with the highest similarity score (cosine similarity).
- **database_handler** - Handles all the interaction with the local SQLite DB.
- **app** - Flask app that displays all the movies on cinema and the recommended movies for a mock user. The user can enter rating on a given movie so that it gets stored in the user DB.
  
## How to run
How to run in the terminal:
```
1. Create a virtual environment and install dependencies
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt

2. Install Chrome browser
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

3. Install chromedriver and add it to ENV
wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
CHROMEDRIVER="path-to-chromedriver"

4. Scrape movies from Filmstaden
python3 scraper.py

5. Create a local DB with a mock user
python3 test_user1.py

6. Run Flask website
flask run
```
## Demo
![Demo](Demo.gif)