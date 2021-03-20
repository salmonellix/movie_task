
from rest_framework import generics, mixins, filters
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieImdbSerializer, MoviesTitlesSerializer, RatingSerializer
from .models import Movie_IMDB



class MovieImdbViewSet(viewsets.ModelViewSet):
    queryset = Movie_IMDB.objects.all().order_by('title')
    serializer_class = MovieImdbSerializer
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


class RatingViewSet(generics.ListAPIView):
    queryset = Movie_IMDB.objects.all()
    serializer_class = RatingSerializer




