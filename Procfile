web: gunicorn blog.wsgi
worker: celery -A blog worker --loglevel=info --concurrency=1 --beat
release: python manage.py migrate