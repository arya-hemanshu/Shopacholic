from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


application = Flask(__name__)
application.config.from_object('settings')

database = SQLAlchemy(application)

migrate = Migrate(application, database)

from Shopacholic.models.item import Item
from Shopacholic.models.order_details import OrderDetails
from Shopacholic.models.product import Product
from Shopacholic.models.product_type import ProductType

from Shopacholic.controllers import home