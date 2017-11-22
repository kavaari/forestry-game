# forestry-game

## Backend
Django setup

0. It's recommended that django is run in virtualenv, however it doesn't affect functionality at all (https://docs.djangoproject.com/en/1.11/topics/install/#installing-official-release)
1. Make sure you have about python 3.5.2 (probably any python 3 works anyways)
2. pip install -r requirements.txt in your virtual env
3. python manage.py makemigrations (prepares database model changes)
3b. python manage.py makemigrations forestry_game
4. python manage.py migrate (executes database changes)
5. Create maps and users for testing python manage.py init_data
6. python manage.py collectstatic (probably not necessary untill deployment)
7. python manage.py runserver 8080
8. Goto localhost:8080 (and hope it works)

Questions and undecided stuff

1. What database (DBMS)?
2. Bootstrap?

## Frontend

https://github.com/gaviarctica/forestry-game-frontend
