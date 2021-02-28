Example for Python/Django (postgres database)

## Start the application

* start postgresql db with docker

* python3 -m venv env

* Mac: source env/bin/activate

  Windows: env/Scripts/activate.bat

* pip install django

* pip install djangorestframework

* Mac: pip install psycopg2-binary

  Windows: pip install psycopg2

* python3.9 manage.py migrate

* python3.9 manage.py runserver

## URLs
* API: http://localhost:8000/api/v1/projects/
* UI: http://localhost:8000/projects/

## Sample payload:

{
"title": "Python examples",
"description": "Python project description",
"technology": "Python",
"image": "project1.png"
}

{
"title": "Java examples",
"description": "Java project description",
"technology": "Java",
"image": "project2.png"
}

{
"title": "Angular examples",
"description": "Angular project description",
"technology": "Angular",
"image": "project3.png"
}

## Blogs
create superuser

```shell script
python manage.py createsuperuser
```

then log in to  http://localhost:8000/admin

## Reference

* https://realpython.com/test-driven-development-of-a-django-restful-api/

* https://realpython.com/get-started-with-django-1/

## Userful commands

* django-admin startproject <project_name>

* python3 manage.py startapp <app_name>

* python3 manage.py makemigrations
