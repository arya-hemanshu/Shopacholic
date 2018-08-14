import os

SECRET_KEY='this-is-my-key'
DEBUG=True
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DATABASE_NAME = 'shopacholic'
DB_HOST = 'localhost'
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER='/static/item_images/'

