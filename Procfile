web: gunicorn events.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate