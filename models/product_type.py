from Shopacholic import database
from datetime import datetime

class ProductType(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    type_name = database.Column(database.String(255))
    timestamp = database.Column(database.DateTime)

    def __init__(self, type_name, timestamp=None):
        self.type_name = type_name
        if timestamp is None:
            self.timestamp = datetime.utcnow()

    def __repr__(self):
        return self.type_name
