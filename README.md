# Meal Helper - Recipe and MealPlan Management System

## Index
- [Summary](#summary)
- [Installation](#installation)
- [Demo](#demo)
- [API Documentation](#api-documentation)

## Summary
Web application for tracking Meals, Foods, MealPlans and Nutritional Information. Built using Django, Django REST Framework, Heroku, Metabase and Swagger

---

## Installation
### Local instructions
- Make sure you have a [Postgres](http://postgresguide.com/) version greater than 9.6
- Clone the repo
- Create your `.env` file by using `.env.example` as template and substituting values based on your environment
- Use [Pyenv](https://github.com/pyenv/pyenv) to install and set Python to version 3.7.x
- Run `pipenv install`
- Activate the virtualenv using `pipenv shell`
- Create development Postgres Database using the command `createdb meal_planner_db` and permissions for user as mentioned in the `meal_planner/settings/dev.py` eg.
    - `$ createdb meal_planner_db`
    - `$ psql -U <user> or $ psql postgres`
    - `# CREATE ROLE meal_planner_app WITH LOGIN PASSWORD 'your-awesome-password';`
    - `# GRANT ALL PRIVILEGES ON DATABASE meal_planner_db TO meal_planner_app;`
    - `# \q`


- Create a superuser using the command `python manage.py createsuperuser`
- Run the local server using the command `python manage.py runserver`
- Hop on to the site and go to `<your-localhost-with-port>/admin`
- Use the above credentials to log into the admin panel

## Demo
- The Backend sandbox can be accessed using Django Admin Panel and [Grappelli](https://django-grappelli.readthedocs.io/en/latest/index.html) at [https://meal-planner-hm.herokuapp.com/](https://meal-planner-hm.herokuapp.com/) with the following credentials:
  - Username: admin@mp.com
  - password: `yummytummy`
- The MetaBase App can be accessed over at [https://meal-helper-metabase-demo.herokuapp.com/](https://meal-helper-metabase-demo.herokuapp.com/) using the following credentials:
  - Username: admin@mp.com
  - Password: `yummytummy1`
- The Database Schema diagram can be found over [here](https://github.com/darth-dodo/meal-helper/blob/master/meal-planner-schema.png)
  

## API Documentation
- [Interactive API Documentation generated using Swagger can be found here](https://meal-planner-hm.herokuapp.com/swagger-docs)
- [API Documentation using the OpenAPI spec can be found over here](https://meal-planner-hm.herokuapp.com/api-docs)

---

## Implementation Choices
- [Python3](https://docs.python.org/3/): Py2 is has reached EoL
- [Pyenv](https://github.com/pyenv/pyenv): For multiple python env management
- [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/): For managing Pip files and environment variables 
- [Postgres](https://www.postgresql.org): Open Source RDBMS Version above 9 to use `jsonb` if required
- [Django](https://docs.djangoproject.com/en/2.2/): Between Bottle, Flask and Django; Django provides a much richer ecosystem and helps the user hit the ground running much faster as compared to Flask. Django 2.2 offers LTS.
- [Grappelli](https://django-grappelli.readthedocs.io/en/latest/index.html): Django Admin Panel replacement. Had to refactor from [Django Jet](https://github.com/darth-dodo/meal-helper/issues/9) as Jet is broken above Django 2.0
- [Django REST Framework](https://www.django-rest-framework.org/): REST APIs with automagical CRUD and extendability
- [DRF JWT](https://github.com/jpadilla/django-rest-framework-jwt): JWT for auth. Need to move towards [SimpleJWT](https://github.com/davesque/django-rest-framework-simplejwt)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/): More efficient debugging + power shell
- [Django Query Count](https://github.com/bradmontgomery/django-querycount): Relatively obscure library which prints out all the queries that happen behind any API request. Helps find bottle necks and duplicated queries
- [Raven/Sentry](https://sentry.io): Capture bugs and stack traces in non prod env
- [Heroku](https://www.heroku.com): Smooth and feature rich PaaS which helps you focus on Dev without fretting a lot about DevOps
- [UnitTest](https://docs.python.org/3/library/unittest.html): Unit Tests for Task 1 using UnitTest Library since it is the standard library and fits the needs for now
- [Django Filter](https://django-filter.readthedocs.io/en/master/): Helps build custom filters which can be dropped in with DRF
- [Swagger UI](https://django-rest-swagger.readthedocs.io/en/latest/): De facto API Documentation Tool
 

