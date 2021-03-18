from django.urls import include, path
from rest_framework import routers


from . import views


from .models import Movie_IMDB
from .views import MovieBestRatedViewSet, AllTitleViewSet, HighestGrossingViewSet, AverageRatingViewSet

router = routers.DefaultRouter()
router.register(r'movies', views.MovieImdbViewSet)
router.register(r'lists', views.MoviesListViewSet)
# router.register(r'movies/all_titles', views.AllTitlesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/best_rated', MovieBestRatedViewSet.as_view()),
    path('movies/all_title', AllTitleViewSet.as_view()),
    path('movies/highest_grossing', HighestGrossingViewSet.as_view()),
    path('movies/average', AverageRatingViewSet.as_view()),

    ]

