# Generated by Django 3.1.7 on 2021-03-18 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_task_api', '0008_auto_20210318_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_imdb',
            name='list_id',
        ),
    ]