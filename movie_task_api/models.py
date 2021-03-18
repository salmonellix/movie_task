from django.db import models
from movie_task_api import fields





class Movie_IMDB(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    imdb_rating = models.FloatField(default=0)
    imdb_id = models.CharField(max_length=100)
    box_office = models.FloatField(default=0)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=100) # or make as choice field but not sure if only 3 types (game, series, film)?
    year = fields.IntegerRangeField(min_value=1, max_value=3000)



    def __str__(self):
        return self.title + str(self.year)


class Movies_List(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    movie_id = models.ManyToManyField(Movie_IMDB)


    def __str__(self):
        return str(self.id)
