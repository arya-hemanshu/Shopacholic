from Shopacholic import database
from datetime import datetime

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    product_type = database.Column(database.Integer, database.ForeignKey('product_type.id'))
    name = database.Column(database.String(255), unique=True)
    image = database.Column(database.String(255))
    short_desc = database.Column(database.Text)
    long_desc = database.Column(database.Text)
    price = database.Column(database.Integer)
    timestamp = database.Column(database.DateTime)

    def __init__(self, product_type, name, image, short_desc, long_desc, price, timestamp=None):
        self.product_type = product_type.id
        self.name = name
        self.image = image
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.price = price
        if timestamp is None:
            self.timestamp = datetime.utcnow()

    def __repr__(self):
        return self.__dict__