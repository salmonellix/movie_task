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


Run Test:
```
    docker-compose exec web python manage.py test
```



