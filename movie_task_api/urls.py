from django.urls import include, path
from rest_framework import routers

from .views import MovieBestRatedViewSet, AllTitleViewSet, HighestGrossingViewSet, AverageRatingViewSet, MovieImdbViewSet, MoviesListViewSet



router = routers.DefaultRouter()
router.register(r'movies', MovieImdbViewSet)
router.register(r'lists', MoviesListViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('movies/best_rated', MovieBestRatedViewSet.as_view()),
    path('movies/all_title', AllTitleViewSet.as_view()),
    path('movies/highest_grossing', HighestGrossingViewSet.as_view()),
    path('movies/ratings', AverageRatingViewSet.as_view()),

    ]

