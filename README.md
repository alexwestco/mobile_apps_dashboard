# Mobile App Analytics Dashboard

A Django and Bootstrap 4 project

## Installation

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).



```sh

$ git clone https://github.com/alexandersideris/mobile_apps_dashboard.git

$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate

$ python manage.py collectstatic

$ python manage.py runserver

```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Documentation

This is the assignment and testable working solution for the Full Stack Developer position. It is also available in a live environment at https://mobile-downloads-dashboard.herokuapp.com/

### What to do

- Read the thoughts and reasoning behind the technical decisions by visiting [localhost:8000/dashboard](localhost:8000/) or [https://mobile-downloads-dashboard.herokuapp.com/dashboard](https://mobile-downloads-dashboard.herokuapp.com/) in a live environment

- View the dashboard

View the dashboard by visiting [localhost:8000/dashboard](localhost:8000/dashboard) or [https://mobile-downloads-dashboard.herokuapp.com/dashboard](https://mobile-downloads-dashboard.herokuapp.com/dashboard) in a live environment

- Seed the database

Populate the database by visiting [localhost:8000/seed_database](localhost:8000/seed_database) or [https://mobile-downloads-dashboard.herokuapp.com/seed_database](https://mobile-downloads-dashboard.herokuapp.com/seed_database) in a live environment

- Check real time updating

The dashboard updates in real time. To see it in action, keep the dashboard open in one window and seed the database in a different window. Notice how the dashboard updates automatically