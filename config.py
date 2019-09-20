import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_user = os.environ.get('DB_USER_TURF')
db_password = os.environ.get('DB_PASSWORD_TURF')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+db_user+':'+db_password+'@nuc:5434/turf_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False