#!/bin/bash


source /root/.local/share/virtualenvs/blog-app-*/bin/activate

echo "<<<<<<<< Collect Staticfiles>>>>>>>>>"
python manage.py collectstatic --noinput