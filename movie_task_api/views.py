from django.shortcuts import render

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