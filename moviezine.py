import requests
from bs4 import BeautifulSoup
#from datetime.datetime import today
import datetime
import pprint
import regex
from user_agent import get_user_agent


def tomorrows_date ():
    date = datetime.datetime.today() + datetime.timedelta(days = 1)
    return datetime.datetime.strftime(date, '%Y-%m-%d')


def query_url():
    return 'https://moviezine.se/kalender/bio'


def _get_headers():
	return {
		# Random generated user agents
		'User-Agent': get_user_agent()
}


def _make_request(url, headers, retries=0) :
	try:
		response = requests.get(url, headers=headers)
	except requests.exceptions.Timeout:
		print("Got a timeout on url " + url)
		if retries >= max_retries:
				raise e
		retries += 1
		return _make_request(url, headers, retries)
	except requests.exceptions.RequestException as e:
		#print("There was an error with getting movies " + url + " on bio.se: " + str(e))
		raise e
	# Check if we wasn't able to acces the content because Pricerunner blocker our IP
	if response.status_code == 403 :
		raise Exception("Staus code was 403 Forbidden.")
	return BeautifulSoup(response.content, features="html.parser")

def parse_movie_specs(movies):
    movie_specs = []
    if movies == []:
        return movie_specs
    for movie in movies:
        movie_specs.append({
        'movie_name': regex.sub(r'\([^)]*\)', '', movie.find('span', class_ = "movie-info__title").text).rstrip(),
        'img_url': movie.find('img')['src']
        })
    return movie_specs

def parse_movies(soup):
    movies = []
    #The main cointainer for all movies
    kalender = soup.find(id = "calender_list_month")
    #Movies are divided by release date, finds all groups
    movies_by_date = kalender.findAll('div', class_ = "list_month_day")
    for movies_same_date in movies_by_date:
        #Example date string is "Onsdag 5 augusti"
        movie_date = movies_same_date.find('h4', class_ = "day").text.split()
        #Only save films that are out already (not future releases)
        if(movie_date[1] <= datetime.datetime.today().day)
            moviez = movies_same_date.findAll('div', class_ = "calender_preview")
            for movie in moviez:
                movies.append({
                'movie_name': "",
                'moviezine_href': 'https://moviezine.se/kalender/bio' + movie.find('a', class_ = "calender")['href'],
                'img_url': movie.find('div', class_ = "cover")['style']
                })


            
    return parse_movie_specs(movies)

def get_movies():
    url = query_url()
    soup = _make_request(
		url,
		headers=_get_headers()
    )
    movies = parse_movies(soup)
    #pprint.pprint(movies)
    return movies
