# prueba-tecnica-quick-python

¡You can run the project soon!, 
only needs install first:

- Clone the project:

```
git clone https://github.com/ariel-david-collab/prueba-tecnica-quick-python.git
```

- Python 3.9.4:

    > can install in the [official page](https://www.python.org/downloads/)

- PostgreSQL 14:

    > [official page](https://content-www.enterprisedb.com/downloads/postgres-postgresql-downloads)

- Django - in the command prompt:
    ```
    > pip install Django
    ```

- The rest_framework for Django:

    ```
    > pip install djangorestframework

    > pip install markdown

    > pip install django-filter
    ```

- PostgreSQL for Django:
    ```
    > pip install psycop2
    ```

- create in postgreSQL an table for the project, can be "prueba-tecnica"

- Reference your database (in the settings.py file):

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "tablename",
        "USER": "username_of_the_postgreSQL_database (default:postgres)",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": '5432",
    }
}
```

- Go in the command prompt to the project in the "manage.py" file location, and run:

    ```
    > python manage.py makemigrations

    > python manage.py migrate
    ```

- Now create an superuser:
    ```
    > python manage.py createsuperuser
    ```

- ¡And run the project!
    ```
    > python manage.py runserver
    ```

## End-points

### Login (/api/v1/users/login)
> method: POST

without Access Token Bearer

```
{
  "mobile_phone": "prueba",
  "password": "prueba"
}
```

### GetUsers (/api/v1/users/)
> method: GET

without Access Token Bearer

### GetUser (/api/v1/users/{id_user}/)
> method: GET

Access Token Bearer required*

### CreateUser (/api/v1/users/)
> method: POST

Access Token Bearer required*

```
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "2021-09-17",
  "mobile_phone": "string",
  "email": "user@example.com",
  "password": "string",
  "address": "stringst"
}
```

### UpdateUser (/api/v1/users/{id_user}/)
> method: PUT

Access Token Bearer required*

```
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "2021-09-17",
  "mobile_phone": "string",
  "email": "user@example.com",
  "password": "string",
  "address": "stringst"
}
```

### DeleteUser (/api/v1/users/{id_user}/)
> method: DELETE

Access Token Bearer required*


