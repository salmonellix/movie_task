# Generated by Django 3.1.7 on 2021-03-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_task_api', '0004_auto_20210318_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_imdb',
            name='title',
        ),
        migrations.AddField(
            model_name='movie_imdb',
            name='title',
            field=models.ManyToManyField(to='movie_task_api.Movies_List'),
        ),
    ]
