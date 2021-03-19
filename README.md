MOVIE TASK :movie_camera:
=====

(IN PROGRESS)



Description
====

This is Django website project that uses Django REST framework.

Thanks to that application u can download and processes information about movies from IMDB.



Run
====
WITH DOCKER:

Build and run:
```
    docker-compose up -d --build
```

Recreate the DB:
```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
```

Check in browser:

[http://localhost:8000](http://localhost:8000)


RUN SCRIPT:
```
    docker-compose exec web python import_data.py command
```
Available commands:

fetch_data + number of movies + movies titles

+ downloads movies from the given list
+ sends GET request to OMDB API 
+ saves selected items by sending POST request to MOVIE TASK API
```
    docker-compose exec web python import_data.py fetch_data 2 "Django" "Pulp Fiction"
```

download_save + format + file_name
+ format options: json, csv, db
+ saving all downloaded movies to a file with the selected format
```
    docker-compose exec web python import_data.py download_save sql my_list
```

titles_list
+ lists all downloaded movie titles
```
    docker-compose exec web python import_data.py titles_list
```

best_rated
+ displays the title of the movie with the highest rating from the downloaded movies
```
    docker-compose exec web python import_data.py best_rated
```

highest_grossing
+ displays top box office movie
```
    docker-compose exec web python import_data.py highest_grossing
```

average_rating
+ shows the average video rating of the downloaded videos
```
    docker-compose exec web python import_data.py average_rating
```

best_rated_IMDB
+ displays the highest rated movie of any movie available on IMDB
```
    docker-compose exec web python import_data.py best_rated_IMDB
```