# Generated by Django 3.1.7 on 2021-03-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_task_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_imdb',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Movies_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ManyToManyField(to='movie_task_api.Movie_IMDB')),
            ],
        ),
    ]
