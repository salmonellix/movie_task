# Generated by Django 3.1.7 on 2021-03-17 21:34

from django.db import migrations, models
import movie_task_api.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_IMDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=130)),
                ('imdb_rating', models.FloatField(default=0)),
                ('imdb_id', models.CharField(max_length=100)),
                ('box_office', models.FloatField(default=0)),
                ('genre', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('year', movie_task_api.fields.IntegerRangeField()),
            ],
        ),
    ]
