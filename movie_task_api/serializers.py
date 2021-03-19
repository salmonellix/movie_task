from rest_framework import serializers

from .models import Movie_IMDB, Movies_List


class MovieImdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= '__all__'


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies_List
        fields= '__all__'


class MoviesTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= ['title']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= ['imdb_rating']