# Generated by Django 3.1.7 on 2021-03-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_task_api', '0006_auto_20210318_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_list',
            name='title',
            field=models.ManyToManyField(related_name='movie_imdb', to='movie_task_api.Movie_IMDB'),
        ),
    ]
