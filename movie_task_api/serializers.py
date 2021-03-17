from rest_framework import serializers

from .models import Movie_IMDB


class MovieImdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_IMDB
        fields= '__all__'