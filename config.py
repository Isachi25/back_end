import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'sachi'
    MYSQL_PASSWORD = 'Today@12345'
    MYSQL_DB = 'merime'