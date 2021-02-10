#!/bin/bash


source /root/.local/share/virtualenvs/blog-app-*/bin/activate

# pipenv shell
echo "<<<<<<<<<< Export LANG to the Env>>>>>>>>>>"

export LC_ALL=C.UTF-8
export LANG=C.UTF-8


echo "<<<<<<<< Collect Staticfiles>>>>>>>>>"
python manage.py collectstatic --noinput


sleep 10
echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"
# Run database migrations
python manage.py migrate


sleep 5
echo "<<<<<<< Database Setup and Migrations Complete >>>>>>>>>>"
echo " "


sleep 5
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
# python manage.py runserver 0.0.0.0:8000
# Start the API with gunicorn
gunicorn --bind 0.0.0.0:8000 blog.wsgi --reload --access-logfile '-' --workers 2