# Generated by Django 3.1.7 on 2021-03-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_task_api', '0005_auto_20210318_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_imdb',
            name='title',
        ),
        migrations.AddField(
            model_name='movie_imdb',
            name='title',
            field=models.CharField(db_index=True, default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='movies_list',
            name='title',
        ),
        migrations.AddField(
            model_name='movies_list',
            name='title',
            field=models.ManyToManyField(to='movie_task_api.Movie_IMDB'),
        ),
    ]