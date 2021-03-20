from django.urls import include, path
from rest_framework import routers

from .views import MovieBestRatedViewSet, AllTitleViewSet, HighestGrossingViewSet, RatingViewSet, MovieImdbViewSet



router = routers.DefaultRouter()
router.register(r'movies', MovieImdbViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('movies/best_rated', MovieBestRatedViewSet.as_view(), name = 'best_rated'),
    path('movies/all_title', AllTitleViewSet.as_view(), name = 'all_titles'),
    path('movies/highest_grossing', HighestGrossingViewSet.as_view(), name='highest_grossing'),
    path('movies/ratings', RatingViewSet.as_view(), name = 'ratings'),

    ]

