# python-django-backendjr-codeleap

Technical test for Codeleap

## Index

- <a href="#-install">Installing and running the project</a>
- <a href="#-requirements">Requirements to run the project</a>
- <a href="#-tech">Technologies</a>
- <a href="#-commands">General commands and Tests</a>

## <h2 id=#-install>Installing and running the project<h2>

```bash
# Use docker-compose build to build the images:
$ docker-compose build

# Start the project with docker compose:
$ docker-compose up

# Acess the docs through your browser:
$ http://localhost:8000/api/docs/

# Utilize the endpoints through Postman or Insomnia:

# Get or Post:
$ http://localhost:8000/api/codeleap/career/
# Patch or Delete:
$ http://localhost:8000/api/codeleap/career/:id/
```

## <h2 id="-requirements">Requisitos do serviço</h2>

This application uses Docker and Docker-compose to run, be sure to have those installed in your machine.

## <h2 id="-tech">Technologies utilized</h2>

- [x] Django
- [x] Django-Rest-Framework
- [x] Psycopg2
- [x] PostgreSQL
- [x] Drf-Spectacular

## <h2 id=#-commands>General commands and Tests<h2>

```bash
# Build or rebuild the images:
$ docker-compose build

# Start the app and the db:
$ docker-compose up

# Shutdown the containers:
$ docker-compose down

# Run tests:
$ docker-compose run --rm app sh -c "python manage.py test"
```
