import sys
import requests
from rest_framework.response import Response
from rest_framework import status



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
        return Response('Server cannot fetch valid data from the API',
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)