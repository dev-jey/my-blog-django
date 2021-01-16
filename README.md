# My Blog

This is a blogging monolithic application created entirely in django.


## Key features included
- Django Signals
- Tinymce
- Cloudinary



### How To Set Up Locally
Install virtualenv
```
pip install virtualenv
```

Create virtual environment
```
virtualenv -p python3 env  && source env/bin/activate
```

Export environment variables
```
export SECRET_KEY=ksksksd
export CLOUD_NAME=ksksksd
export API_KEY=ksksksd
export API_SECRET=ksksksd
export DB_NAME=llll
export DB_USER=ksksksd
export DB_PASS=ksksksd
export DB_HOST=ksksksd
export DB_PORT=ksksksd
export CURRENT_BACKEND_URL=ksksksd
```

Install dependencies
```
pip install -r requirements.txt
```

Load static files 
```
python manage.py collectstatic
```

Run the server
```
python manage.py runserver
```