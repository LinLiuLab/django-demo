# Django Demo

Demo of Django for the [Software Engineering 2023](https://linliulab.github.io/SE-2023/) course.

## Pre-requisites

-   Python 3.8 or above

## Quick Start(Docker)

```bash
docker-compose up
```

## Quick Start(Manual)

1. Clone this repository

```bash
git clone https://github.com/linliulab/django-demo.git
```

2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

3. Initialize the database

-   Create a database named `django_demo` in MySQL
-   Edit the database connection string in `django_demo/settings.py` (line 82 - 89)

4. Run the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
