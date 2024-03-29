import os

from celery import Celery

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')


DROPBOX_CLIENT_ID = os.getenv('DROPBOX_CLIENT_ID')
DROPBOX_CLIENT_SECRET = os.getenv("DROPBOX_CLIENT_SECRET")



RABBIT_URL = 'amqp://' + os.getenv('RABBITMQ_USER') + ':' + os.getenv('RABBITMQ_PASSWORD') + '@' + os.getenv(
    'RABBITMQ_HOST') + ':' + os.getenv('RABBITMQ_PORT')


print(DB_HOST, DB_NAME, DB_HOST, DB_PORT, DB_USER)

