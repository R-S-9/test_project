# Instructions for the developer
## Installing dependencies
```
pip install -r requirements.txt
```
## Launch surrounded by the developer
Create a database in PostgreSQL and point to `settings.py`. Example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testproject',
        'USER': 'postgres',
        'PASSWORD': 'Origin123',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```
Launch:
```
cd src
python manage.py runserver --insecure
```
