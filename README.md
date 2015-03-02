# Image Detection Web Service

## Requirements
You'll need to have PostgreSQL installed. You can use the standalone Mac application [Postgres.app](http://postgresapp.com/).

If you choose to use Postgres.app, make sure you have the right binaries in your path. Instructions for doing this are documented
on [the postgresapp website](http://postgresapp.com/documentation/cli-tools.html).


## Installation
The following will install all python dependencies, setup the database user & db, and apply all migrations.

    ./bootstrap.sh


# Running the server
The actual Django project lives in the `detectweb` directory. You can run the web application locally by running the following:

    python manage.py runserver


# Migrations
Every change to the models will require a database migration. If the project's models have been updated, you can migrate the database
by issuing the following command:

    python manage.py migrate

Migrations are not created automatically. Once you're done making changes to the models, you can create the necessary migration files by
issuing the following command:

    python manage.py makemigrations <app_name>

See more [here](https://docs.djangoproject.com/en/1.7/ref/django-admin/#django-admin-makemigrations);


# Celery

To run the server, run this command:

    celery -A detectweb worker --loglevel=info

Once the celery server is running, you can run a job:

```
from detectweb.tasks import do_matlab
a = do_matlab.delay('test')
```

# Running tests

    python manage.py test
