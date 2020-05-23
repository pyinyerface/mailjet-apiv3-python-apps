from django_app.celery import app
from mailjet_rest import Client
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)

@app.task(bind=True)
def welcome_registered_user(self, email, username):
    
    mailjet_apikey = settings.MAILJET_APIKEY
    mailjet_apisecret = settings.MAILJET_APISECRET
    mailjet_sender = settings.MAILJET_SENDER

    if any([not var for var in [mailjet_apikey, 
                                    mailjet_apisecret, 
                                    mailjet_sender]]):
        logger.info("Unable to send welcome email because MAILJET_APIKEY, MAILJET_APISECRET and/or MAILJET_SENDER is null.")
        return
    
    try:
        mailjet_api = Client(auth=(mailjet_apikey, 
                            mailjet_apisecret), version='v3.1')
    except Exception as e:
        logger.error(f"Unable to send welcome email because an exception occurred during Mailjet authentication: {e}")
        return

    data = {
                'Messages': [
                    {
                            "From": {
                                    "Email": mailjet_sender,
                                    "Name": "PyInyerface"
                            },
                            "To": [
                                    {
                                            "Email": email,
                                            "Name": username
                                    }
                            ],
                            "Subject": "Welcome",
                            "HTMLPart": "<p>Thanks for registering to our app!</p>"
                    }
            ]
    }
    
    result = mailjet_api.send.create(data=data)

    logger.info(f"Mailjet welcome email result: {str(result)}")
    



