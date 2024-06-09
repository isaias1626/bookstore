release: python manage.py migrate
web: gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT