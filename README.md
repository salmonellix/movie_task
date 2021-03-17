MOVIE TASK
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

Recreate the DB
```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
```

