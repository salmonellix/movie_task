from django.db import models
from movie_task_api import fields


class Movie_IMDB(models.Model):
    title = models.CharField(max_length=130, db_index=True)
    imdb_rating = models.FloatField(default=0)
    imdb_id = models.CharField(max_length=100)
    box_office = models.FloatField(default=0)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = fields.IntegerRangeField(min_value=1, max_value=3000)


    def __str__(self):
        return self.title + str(self.year)






