import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LANGUAGES = ['en', 'de']
    YANDEX_TRANSLATOR_KEY = 'trnsl.1.1.20180608T094519Z.8c39a6df739bccae.58d436ef98b8aafddda1f951aef0b4ae7f13a562'

