import database_handler as db
from scraper import scraper 
from website import app
from recommender import recommender


if __name__ == '__main__':
    scraper = scraper.WebScraperAgent()
    scraper.start()
    database = db.DatabaseHandler()
    database.start()
    website = app.Website()
    website.start()
