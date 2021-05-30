## Cinema recommender

A cinema recommender implemented in Flask.
By scraping current movies on cinema (Filmstaden), the user gets recommendations based on similarity score with previously watched movies.
The architecture is a multi-agent system (mas) that consists of: 
* Web scraping agent
* Recommendation agent
* Website agent
* Local database

## Code functionality 
- **scraper (agent)** - Scrapes current movies from Filmstaden and stores the information locally.
- **recommender (agent)** - Finds current movies with the highest similarity score (cosine similarity) based on a user's previously seen movies and ratings.
- **website (agent)** - Displays all the movies on cinema and the recommended movies for a user. The user can also rate movies on the website which are persisted in the DB.
- **database** - Handles all the interaction with the local SQLite DB.
- **mas** -  Coordinates the agents to scrape, recommend and display the website.
  
## How to run
How to run in the terminal:
```
1. Create a virtual environment and install dependencies
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt

2. Install Chrome browser
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb

3. Install latest chromedriver and add it to ENV
$ version=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
$ wget "https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip"
$ unzip chromedriver_linux64.zip
$ CHROMEDRIVER="path-to-chromedriver"

4. Run multi-agent system  
(env) $ python3 mas.py
```
## Demo
<img src=Demo.gif width=100% height=100%>
