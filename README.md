# graphql-python-meetup
Example demo project for GraphQL talk at Barcelona Python Meetup

Contains two apps: One with Django models and a second one without.

Install instructions:

 * Create a Python virtual environment
 * Install requirements: `pip install -r requirements.txt`

## plain - without Django models

This app takes the data from a dictionary. To run it just do:
```
python app.py runserver
``` 
And visit http://localhost:8000/graphql/ in your browser.


## djproject - with Django models

 * `python manage.py migrate`
 * `python manage.py createsuperuser`
 * `python manage.py runserver`
 * Go to http://localhost:8000/admin, use the credentials you just generated and create some Products, Reviews and/or Users
 
