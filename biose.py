import requests
from bs4 import BeautifulSoup
#from datetime.datetime import today
import datetime
import pprint
from user_agent import get_user_agent


def tomorrows_date ():
    date = datetime.datetime.today() + datetime.timedelta(days = 1)
    return str(datetime.datetime.strftime(date, '%Y-%m-%d'))


def query_url():
    date = tomorrows_date()
    return 'https://bio.se/filmer/{0}'.format(date)


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
        'movie_name': movie.find('span', class_ = "movie-info__title").text,
        'img_url': movie.find('img')['src']
        })
        print(movie_specs)
    return movie_specs

def parse_movies(soup):
    movies = []
    movies = soup.findAll('div', class_ = "movie col-6 col-md-4 col-lg-3 col-xl-2")
    return parse_movie_specs(movies)

def get_movies():
    url = query_url()
    soup = _make_request(
		url,
		headers=_get_headers()
    )
    movies = parse_movies(soup)
    pprint.pprint(movies)


get_movies()
