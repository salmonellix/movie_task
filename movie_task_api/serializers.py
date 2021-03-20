from rest_framework import serializers

from .models import Movie_IMDB


class MovieImdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= '__all__'


class MoviesTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= ['title']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= ['imdb_rating']