Sample for Python/Django REST API (postgres database)

start postgresql db with docker

python3 -m venv env

For Mac: source env/bin/activate

For Windows: env/Scripts/activate.bat

pip install django

pip install djangorestframework

For Mac: pip install psycopg2-binary

For Windows: pip install psycopg2

python3.9 manage.py migrate

python3.9 manage.py runserver

Reference:
https://realpython.com/test-driven-development-of-a-django-restful-api/

Sample payload:
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

## Reference

https://realpython.com/get-started-with-django-1/
