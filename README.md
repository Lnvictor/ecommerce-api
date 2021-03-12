# Ecommerce API

A simple ecommerce API using django rest framework

## Requirements
- python 3

## Installation
1. Clone this repository:
```console
    git clone https://github.com/Lnvictor/ecommerce-api
```

2. Install the project requirements from requirements.txt file:
```console
    pip install -r requirements.txt
```

3. Set the following env variables in .env file in project root:
```
    SECRET_KEY=
    DATABASE_URL=
    DEBUG=
    ALLOWED_HOST 
```

4. Apply the migrations:
```console
    python manage.py migrate
```

## How to run

Just run the following command and have fun :heart:

```console
    python manage.py runserver
```

## Making requests
To send requests to any API endpoint, you should has an api_key,
you can create with this following commands:

```console
python manage.py shell
```

Then create your key:
```python
from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="my-remote-service")
```

## References

- [Django Official Documentation](https://docs.djangoproject.com/en/3.1/)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/)