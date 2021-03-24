from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .models import Movie_IMDB
from rest_framework.test import APIClient, APIRequestFactory, RequestsClient
import responses
import requests
from rest_framework import status
import json

class TestMovieTaskApi(TestCase):

    # response = responses.RequestsMock()

    @classmethod
    def setUpClass(cls):
        super(TestMovieTaskApi, cls).setUpClass()

        movie = Movie_IMDB.objects.create(title="Django", imdb_rating=7.2, imdb_id = "tt0060315", box_office = 6.0,
                                          genre = "Action, Western", type = "movie", year = 1966)

    def test_fetch_create_movie(self):
        client = APIClient()
        response = client.post('/movies/', data={'title': 'Pulp Fiction'}, format='json')
        response2 = client.get('/movies/2/')
        json_resp2 = response2.json()
        self.assertEquals(201, response.status_code)
        self.assertEquals('Pulp Fiction', json_resp2['title'])


    def test_get_list_movie(self):
        client = APIClient()
        response = client.get('/movies/')
        self.assertEquals(200, response.status_code)
        # self.assertEquals(1, len(response.json()))
        movie = response.json()[0]
        self.assertEquals('Django', movie['title'])

    def test_delete_movie(self):
        client = APIClient()
        response = client.delete('/movies/1/')
        self.assertEquals(204, response.status_code)
        response = client.get('/movies/')
        self.assertEquals([], response.json())




