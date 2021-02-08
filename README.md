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
source env/bin/activate
export SECRET_KEY=seckey
export CLOUD_NAME=cloudinary_name
export API_KEY=cloudinary_api_key
export API_SECRET=api_secret
export DB_USER=db_user
export DB_PASSWORD=db_pass
export DB_HOST=localhost
export DB_NAME=name_of_db
export CURRENT_ENV=development
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