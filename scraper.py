import requests
from bs4 import BeautifulSoup
import datetime
import pprint
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
import csv

def tomorrows_date ():
    date = datetime.datetime.today() + datetime.timedelta(days = 1)
    return datetime.datetime.strftime(date, '%Y-%m-%d')


def start_url():
    return 'https://www.filmstaden.se/filmer-och-trailers/'

def query_movie_page(href):
    return f"https://www.filmstaden.se{href}" 


def get_driver():
    #DRIVER_PATH = "/home/natan/Downloads/geckodriver"
    #driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options,executable_path="/usr/lib/chromium-browser/chromedriver")
    driver.get(start_url())
    time.sleep(1) 
    button = driver.find_element_by_xpath('//*[@id="Aurelia"]/div[3]/div/div/div[2]/span/button')
    button.click()
    return driver

def get_all_movie_links(page_source):
    soup = BeautifulSoup(page_source,features="html.parser")
    all_movies_div = soup.find('div',class_="all-movies")
    movies = all_movies_div.find_all('li',class_="all-movies__list-thumbnail-item")
    all_links = []
    for movie in movies:
        link = movie.find('a')["href"]
        all_links.append(link)
    return all_links


#the genre section can have multiple genres, so we need them all
def get_genre(soup):
    genre = ""
    try:
        first_genre = soup.find_all('div',class_="au-target movie-information__poster-section-genre") #this is a list of all the genres for the movie besides the last one
        for val in first_genre:
            genre = genre + val.text
        last_genre = soup.find('div',class_="au-target movie-information__poster-section-genre movie-information__genre--last").text
        return genre + last_genre 
            
    except:
        return soup.find('div',class_="au-target movie-information__poster-section-genre movie-information__genre--last").text

def get_movie_info(driver,href):
    driver.get(query_movie_page(href))
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source,features="html.parser")
    try:
        body_div = soup.find('div',class_='movie-information__body-section block__wrapper block__wrapper--regular')
        movie_description = body_div.find('div',class_="movie-information__long-description au-target").find('p').get_text()
        attribute_div = body_div.find_all('div',class_="movie-information__meta-attributes")
        genre = get_genre(soup)
        info = []
        for attribute in attribute_div:
            values = attribute.find_all('div',class_="movie-information__meta-attributes-value")
            text = ""
            for value in values:
                text = text + value.text
            info.append(text)

        all_info = {"Directors":info[0],"Actors":info[1],"Genre":genre,"Original_title":info[2],"Original_language":info[3],"Date":info[4],"Description":movie_description}
        return all_info
    except Exception as e:
        print("Some info  for this movie is missing for this movie probably, so it will be skipped :)")
        print(e)
        return None

def write_csv(all_info):
    with open ("filmstaden.csv",mode="w") as csv_file:
        fieldnames = ["Directors","Actors","Genre","Original_title","Original_language","Date","Description"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for val in all_info:
            if val is not None:
              writer.writerow(val)
    
    
if __name__ == "__main__":
    driver = get_driver()
    movie_links = get_all_movie_links(driver.page_source)
    all_movies_info = []
    for link in movie_links:
        info = get_movie_info(driver,link)
        all_movies_info.append(info)

    write_csv(all_movies_info)
    
    
