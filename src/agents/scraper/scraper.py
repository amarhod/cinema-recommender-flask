import requests
import datetime
import pprint
import time
import csv
import os
import logging
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

DRIVER = os.getenv('CHROMEDRIVER')

logging.basicConfig()
logging.root.setLevel(20)
logger = logging.getLogger(' Web-scraping agent ')



class WebScraperAgent():
    def __init__(self):
        logger.info('[Configuration] Configuring web-scraping agent')
        self.driver = get_driver()
    
    def start(self):
        logger.info('[Initialization] Starting agent')
        self.get_initial_state()
        self.all_movies = self.goal_search()
        self.store()
        self.end()
    
    def end(self):
        logger.info('[End state] Shutting down agent')
        self.driver.close()

    def store(self):
        logger.info('[Store] Storing enumerated movies in CSV file')
        write_csv(self.all_movies)

    def get_initial_state(self):
        """Visit Filmstadens website and accept cookies and city preference"""
        logger.info('[Initial state] Browsing to Filmstaden')
        self.driver.get(start_url())
        try:
            time.sleep(3)
            button = self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
            button.click()
            time.sleep(1)
            button = self.driver.find_element_by_xpath('//*[@id="Aurelia"]/div[2]/div/div/div[2]/span/button')
            button.click()
        except:
            print("button click failed")
            logger.error('Failed to accept cookies and save city on Filmstadens website')

    def goal_search(self):
        logger.info('[Searching state] Enumerating all movies')
        movie_links = get_all_movie_links(self.driver.page_source)
        all_movies_info = []
        index = 1
        for link in movie_links:
            info = get_movie_info(self.driver, link)
            if info is not None:
                title = info['Original_title']
                logger.info(f'[Searching state] Found movie "{title}"')
                info["Index"] = index
                index = index + 1
                all_movies_info.append(info)
        return all_movies_info


def start_url():
    """Returns first page URL for Filmstaden

    Returns:
        String: URL for the front page of Filmstaden
    """    
    return 'https://www.filmstaden.se/filmer-och-trailers/'

def query_movie_page(href):
    """Returns the URL for a movie given its unique href

    Args:
        href (String): Unique identifier for a movie

    Returns:
        String: URL for a movie page
    """            
    return f"https://www.filmstaden.se{href}" 

def get_driver():
    """Starts a Chrome webdriver

    Returns:
        webdriver: Chrome webdriver
    """    
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(options=chrome_options, executable_path=DRIVER)
    except:
        logger.error('Chromedriver was not found')
    return driver

def get_all_movie_links(page_source):
    """Returns the list of all hrefs needed to visit each movie

    Args:
        page_source (BeautifulSoup): A soup object containing the HTML for the 'movies' page

    Returns:
        list: list of all movie hrefs
    """
    soup = BeautifulSoup(page_source,features="html.parser")
    all_movies_div = soup.find('div',class_="all-movies")
    movies = all_movies_div.find_all('li',class_="all-movies__list-thumbnail-item")
    all_links = []
    for movie in movies:
        link = movie.find('a')["href"]
        all_links.append(link)
    return all_links

def get_genre(soup):
    """Returns all the genres for a given movie

    Args:
        soup (BeautifulSoup): A soup object containing the HTML for a movie

    Returns:
        String: A string containing all the genres for a given movie
    """    #
    genre = ""
    try:
        first_genre = soup.find_all('div',class_="au-target movie-information__poster-section-genre") #this is a list of all the genres for the movie besides the last one
        for val in first_genre:
            genre = genre + val.text
        last_genre = soup.find('div',class_="au-target movie-information__poster-section-genre movie-information__genre--last").text
        return genre + last_genre  
    except:
        return soup.find('div',class_="au-target movie-information__poster-section-genre movie-information__genre--last").text


def download_image(url):
    """Stores the movie cover poster images locally in Flask/static/image

    Args:
        url (String): URL to the image
    """    
    if(url == None):
        print("empty img url")
        return
    url_path=url.split('/')
    #https......./2k6h41.jpg -> 2k6h41
    name = url_path[len(url_path)-1]
    #print(os.path.abspath(os.getcwd()))
    static_path = 'website/static/images/'+name
    try:
        f = open(static_path,'rb')
        f.close()
        print("image already stored")
    except:
        request = requests.get(url)
        f = open(static_path, 'wb')
        f.write(request.content)
        f.close()
    return

def get_movie_info(driver, href):
    """Returns a dictionary with info about a given movie 

    Args:
        driver (webdriver): Chrome webdriver
        href (String): Unique identifier for a movie

    Returns:
        Dictionary: a dictionary with info about the movie
    """    
    driver.get(query_movie_page(href))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,features="html.parser")
    try:
        body_div = soup.find('div',class_='movie-information__body-section block__wrapper block__wrapper--regular')
        movie_description = body_div.find('div',class_="movie-information__long-description au-target").find('p').get_text()
        attribute_div = body_div.find_all('div',class_="movie-information__meta-attributes")
        genre = get_genre(soup)
        info = []
        labels = ["Svenska röster:","Originalröster:"] #we want to skip movies that have this labels instead of the actors lable
        for attribute in attribute_div:
            lables_list = attribute.find_all('div',class_="movie-information__meta-attributes-label") #find all lables to check if one of them is in our black list of lables
            for lable in lables_list:
                if lable.text.strip() in labels:
                    #print("Movie without actors, will be skipped!")
                    return None
            values = attribute.find_all('div',class_="movie-information__meta-attributes-value")
            text = ""
            for value in values:
                text = text + value.text
            info.append(text.strip())
        #Extract the cover image link
        try:
            img_body_div = soup.find('div',class_='movie-information__top-section')
            img_url_src = img_body_div.find('img', class_='movie-information__poster-section-image au-target')['src']
            img_url = img_url_src.split('?')[0]
            download_image(img_url)
        except Exception as e:
            print(e.stacktrace())
            img_url ="FAILED_EXTRACTION"
        all_info = {"Directors":info[0],"Actors":info[1],"Genre":genre,"Original_title":info[2],
        "Original_language":info[3],"Date":info[4],"Description":movie_description,"Img_url": img_url}
        return all_info
    except Exception as e:
        #print(e)
        return None

def write_csv(all_info):
    """Stores a list of movies in a CSV file

    Args:
        all_info (List): A list containing all the movies found
    """    
    with open ("scraper/filmstaden.csv", mode="w") as csv_file:
        fieldnames = ["Index","Directors","Actors","Genre","Original_title","Original_language","Date","Description","Img_url"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for val in all_info:
            writer.writerow(val)

    
if __name__ == "__main__":
    scraper = WebScraperAgent()
    scraper.start()
