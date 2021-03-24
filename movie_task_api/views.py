
from rest_framework import generics, mixins, filters
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from movie_task_api.fetch_data import get_movie_info
from .serializers import MovieImdbSerializer, MoviesTitlesSerializer, RatingSerializer
from .models import Movie_IMDB
from requests import RequestException



class MovieImdbViewSet(viewsets.ModelViewSet):
    queryset = Movie_IMDB.objects.all().order_by('title')
    serializer_class = MovieImdbSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        title = request.data.get('title')

        if not title:
            return Response('Title is required.', status=status.HTTP_400_BAD_REQUEST)

        movie = Movie_IMDB.objects.filter(title=title).first()

        if movie:
            serializer = self.get_serializer(movie)
            return Response(serializer.data, status=200)

        else:

            try:
                data = get_movie_info(title)
            except RequestException:
                return Response('API service is unreachable.', status=status.HTTP_503_SERVICE_UNAVAILABLE)
            except RuntimeError:
                return Response(f'Movie not found, {title}', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Server cannot fetch valid data from the API',
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            serializer = self.get_serializer(data=data)

            if not serializer.is_valid():
                return Response('Server cannot fetch valid data from the API',
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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




