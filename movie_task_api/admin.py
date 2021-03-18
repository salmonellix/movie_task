from django.contrib import admin
from .models import Movie_IMDB, Movies_List

admin.site.register(Movies_List)
admin.site.register(Movie_IMDB)