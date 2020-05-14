#!/usr/bin/env python
import os
from app import celery, create_app

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)

# MAIL_PASSWORD was generated form https://myaccount.google.com/apppasswords
# only if 2fa is there for the google account

# print('dot env?')
# print(os.getenv('MAIL_USERNAME'))
# print(os.getenv('MAIL_PASSWORD'))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()
