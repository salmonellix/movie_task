from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, mixins, filters
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

class MovieImdbViewSet(viewsets.ModelViewSet):
    queryset = Movie_IMDB.objects.all().order_by('title')
    serializer_class = MovieImdbSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class MoviesListViewSet(viewsets.ModelViewSet):
    queryset = Movies_List.objects.all().order_by('title')
    serializer_class = MoviesListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']



class MovieBestRatedViewSet(APIView):

    def get(self,request):
        queryset = Movie_IMDB.objects.latest('imdb_rating')
        serializer = MovieImdbSerializer(queryset)
        return Response(serializer.data)

class AllTitleViewSet(generics.ListAPIView):
    queryset = Movie_IMDB.objects.all()
    serializer_class = MoviesTitlesSerializer


class HighestGrossingViewSet(APIView):

    def get(self,request):
        queryset = Movie_IMDB.objects.latest('box_office')
        serializer = MovieImdbSerializer(queryset)
        return Response(serializer.data)

class AverageRatingViewSet(generics.ListAPIView):
    queryset = Movie_IMDB.objects.all()
    serializer_class = RatingSerializer







