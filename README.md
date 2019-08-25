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
- The MetaBase App can be accessed over [here]() using the following credentials:
  - Username: admin@mp.com
  - Password: `yummytummy1`
- The Database Schema diagram can be found over [here](https://github.com/darth-dodo/meal-helper/blob/master/meal-planner-schema.png)
  

## API Documentation
- [Interactive API Documentation generated using Swagger can be found here](https://meal-planner-hm.herokuapp.com/swagger-docs)
- [API Documentation using the OpenAPI spec can be found over here](https://meal-planner-hm.herokuapp.com/api-docs)

## Task 1 Implementation
- Task 1 is implemented on the [`free` action](https://github.com/darth-dodo/meal-helper/blob/master/meals/views.py#L105) of the Meal ViewSet
- It can be access using Postman with the following URL: [https://meal-planner-hm.herokuapp.com/api/meals/meal/free?food_ids=1,11](https://meal-planner-hm.herokuapp.com/api/meals/meal/free?food_ids=1,11)
- The task has been reimplemented using DRF and Django Filters. Please check out the Swagger Docs for the implementation details

