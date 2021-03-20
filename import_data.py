import json
import sys
import pandas as pd
from sqlalchemy import create_engine
import requests


def get_movie_info(title):

    #api key:
    my_key = '9e827d46'
    get_response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey={my_key}')

    # extracting data in json format
    fetched_data = get_response.json()
    data = {field.lower(): value for field, value in fetched_data.items()}

    try:
        data = {k: 0 if v == 'N/A' else v for k, v in data.items()}
    except:
        pass

    try:
        if data['type'] != 'movie':
            print(title + " Not a movie")
        else:
            parsed_values = {
                'title': data['title'],
                'imdb_rating': float(data['imdbrating']),
                'imdb_id': data['imdbid'],
                'year': int(data['year']),
                'box_office': float(data['boxoffice'].replace(',','')[-1]),
                'genre': data['genre'],
                'type': data['type'],

            }
            return parsed_values
    except:
        print("Cant fetch data")




# dowload data from IMDB using OMDB API and save to MOVIE TASK API
def fetch_data():

    movies_nbr = int(sys.argv[2])

    for nbr in range(0,movies_nbr):
        title = sys.argv[3 + nbr]
        print(title)
        movie_info = get_movie_info(str(title))

        if movie_info:

            # post api-endpoint
            API_ENDPOINT = "http://127.0.0.1:8000/movies/"

            get_response = requests.post(url=API_ENDPOINT, data=movie_info)
            api_response = get_response.text
            print("API response is:%s" % api_response)


# print all saved titles
def titles_list():

    # send get request to get all titles
    get_response = requests.get("http://127.0.0.1:8000/movies/all_title")
    api_response = get_response.json()
    # print all movies titles
    for movie in api_response:
        print(movie["title"])


# best rated movie from saved database
def best_rated():

    get_response = requests.get("http://127.0.0.1:8000/movies/best_rated")
    api_response = get_response.json()
    print(api_response["title"])


########### use only when Pandas instaled
# best rated movies from IMDB databsae
def best_rated_IMDB():

    best_IMDB_movie = pd.read_html("https://www.imdb.com/chart/top/?ref_=nv_mv_250/")
    print('Best rated movie from IMDB')
    print(f'TITLE: {best_IMDB_movie[0]["Rank & Title"].iloc[0]}' )
    print(f'RATING: {best_IMDB_movie[0]["IMDb Rating"].iloc[0]}')


# movie with highest box office from saved movies
def highest_grossing():

    get_response = requests.get("http://127.0.0.1:8000/movies/highest_grossing")
    api_response = get_response.json()
    print(api_response["title"])
    print(api_response["box_office"])


# average rating based on saved movies
def average_rating():

    get_response = requests.get("http://127.0.0.1:8000/movies/ratings")
    api_response = get_response.json()
    all_ratings = 0

    for rating in api_response:
        all_ratings += float(rating["imdb_rating"])
    print(f"Average rating: {all_ratings/len(api_response)}", )


# dowload saved movie 3 options
def download_save():

    format_name = str(sys.argv[2])
    file_name = str(sys.argv[3])
    get_response = requests.get("http://127.0.0.1:8000/movies/")
    api_response = get_response.json()

    if format_name == 'json':
        with open(f'{file_name}.json', 'w') as json_file:
            json.dump(api_response, json_file)

    elif format_name == 'csv':
        file = pd.read_json(json.dumps(api_response))
        file.to_csv(f'{file_name}.csv')

    elif format_name == 'sql':

        data_df = pd.DataFrame(api_response)

        engine = create_engine(f"sqlite:///{file_name}.db")
        data_df.to_sql("table_name", con=engine)




## command options
COMAND = str(sys.argv[1])

if COMAND == 'fetch_data':
    fetch_data()

if COMAND == 'titles_list':
    titles_list()

if COMAND == 'best_rated':
    best_rated()

if COMAND == 'highest_grossing':
    highest_grossing()

if COMAND == 'average_rating':
    average_rating()

if COMAND == 'best_rated_IMDB':
    best_rated_IMDB()

if COMAND == 'download_save':
    download_save()