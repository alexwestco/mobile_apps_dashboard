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

- View the dashboard

View the dashboard by visiting "localhost:8000/dashboard"

- Seed the database

Populate the database by visiting "localhost:8000/seed_database"

- Check real time updating

The dashboard updates in real time. To see it in action, keep the dashboard open in one window and seed the database in a different window. Notice how the dashboard updates automatically