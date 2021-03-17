from django.urls import include, path
from rest_framework import routers


from . import views


from .models import Movie_IMDB

router = routers.DefaultRouter()
router.register(r'movies', views.MovieImdbViewSet)
# router.register(r'students', views.StudentViewSet)
# router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]