import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Shopacholic import application
import sqlalchemy

db_uri = 'mysql+pymysql://%s:%s@%s/' % (application.config['DB_USERNAME'], application.config['DB_PASSWORD'], application.config['DB_HOST'])
db_engine = sqlalchemy.create_engine(db_uri)
connection = db_engine.connect()
databases = connection.execute('show databases;')
does_exist = False
for d in databases:
    if d[0] == application.config['DATABASE_NAME']:
        does_exist = True
        break

connection.execute('commit')
if does_exist:
    connection.execute('drop database ' + application.config['DATABASE_NAME'])
connection.execute('create database ' + application.config['DATABASE_NAME'])
connection.close()