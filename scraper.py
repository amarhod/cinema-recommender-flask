import requests
import datetime
import pprint
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options


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
    driver = webdriver.Chrome(options=chrome_options,executable_path="/usr/local/bin/chromedriver")
    driver.get(start_url())
    #click on  the accept cookie button,
    try:
        time.sleep(2) #not the best way but waiting for loading doesnt seem to do the trick
        but = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
        but.click()
        time.sleep(2)
        #click on the save region button
        button = driver.find_element_by_xpath('//*[@id="Aurelia"]/div[2]/div/div/div[2]/span/button')
        button.click()
    except:
        print("button click failed")    
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

#The genre section can have multiple genres, so we need them all
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

#Stores the cover poster images locally in Flask/static/image
def download_image(url):
    if(url == None):
        print("empty img url")
        return None
    url_path=url.split('/')
    #https......./2k6h41.jpg -> 2k6h41
    name = url_path[len(url_path)-1]
    static_path = 'Flask/static/images/'+name
    try:
        f = open(static_path,'rb')
        f.close()
        print("image already stored")
    except:
        request = requests.get(url)
        f = open(static_path, 'wb')
        f.write(request.content)
        f.close()

def get_movie_info(driver,href):
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
                    print("Movie without actors, will be skipped!")
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
        except:
            img_url ="FAILED_EXTRACTION"
        all_info = {"Directors":info[0],"Actors":info[1],"Genre":genre,"Original_title":info[2],
        "Original_language":info[3],"Date":info[4],"Description":movie_description,"Img_url": img_url}
        return all_info
    except Exception as e:
        print("Some info  for this movie is missing for this movie probably, so it will be skipped :)")
        print(e)
        return None

def write_csv(all_info):
    with open ("filmstaden.csv",mode="w") as csv_file:
        fieldnames = ["Index","Directors","Actors","Genre","Original_title","Original_language","Date","Description","Img_url"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for val in all_info:
            writer.writerow(val)

def get_list():
    driver = get_driver()
    movie_links = get_all_movie_links(driver.page_source)
    all_movies_info = []
    index = 1
    for link in movie_links:
        info = get_movie_info(driver,link)
        if info is not None:
            info["Index"] = index
            index = index + 1
            all_movies_info.append(info)
    #pprint.pprint(all_movies_info)
    write_csv(all_movies_info)
    return all_movies_info
    
    
if __name__ == "__main__":
    pprint.pprint(get_list())
