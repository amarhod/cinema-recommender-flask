import database.database_handler as db
from agents.scraper import scraper 
from agents.website import app
from agents.recommender import recommender


if __name__ == '__main__':
    scraper = scraper.WebScraperAgent()
    scraper.start()
    database = db.DatabaseHandler()
    database.start()
    website = app.Website()
    website.start()
