# mailjet-apiv3-python-apps
Apps that utilize [mailjet's python API wrapper](https://github.com/mailjet/mailjet-apiv3-python)

## Requirements
 - Mailjet Account
 - Python 3.6
 - Pip dependencies (run 'pip install -r requirements.txt' in 
    ./mailjet-apiv3-python-apps)

## How to setup Mailjet

 - Login/register-then-login to a Mailjet account.
 - Add a sender domain or Address
 - Retrieve your API Key and Secret from "SMTP and SEND API Settings"

## How to use Django app

 - Scroll all the way to the bottom of mailjet-apiv3-python-apps/django_app/django_app/settings.py and set the mailjet variables (MAILJET_SENDER, MAILJET_API_KEY and MAILJET_API_SECRET).
 - Run 'python manage.py makemigrations', 'python manage.py migrate' and finally, 'python manage.py runserver'. 
 - Go to 'localhost:8000' in your browser and you should see a 'Django Rest Framework page'.
 - You can test the Mailjet sender by registering a user. A "Welcome" message should arrive in your inbox shortly after clicking "Submit".