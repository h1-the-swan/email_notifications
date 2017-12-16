import os
from dotenv import load_dotenv
status = load_dotenv('.env')
if not status:
    raise RuntimeError("failed to load .env")

SMTP_ARGS = {
    'mailhost': 'smtp.gmail.com',
    'fromaddr': os.environ['EMAIL_NOTIFICATION_USERNAME'],
    'toaddrs': ['jporteno@uw.edu'],
    'subject': 'New Event From [APPLICATION]',
    'credentials': (os.environ['EMAIL_NOTIFICATION_USERNAME'], os.environ['EMAIL_NOTIFICATION_PASSWORD']),
    'secure': tuple()
}

import logging
from logging.handlers import SMTPHandler
email_handler = SMTPHandler(**SMTP_ARGS)
email_logger = logging.getLogger('email_logger')
email_logger.addHandler(email_handler)
email_logger.setLevel = logging.INFO
email_logger.propagate = False
