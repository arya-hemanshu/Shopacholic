from Shopacholic import database
from datetime import datetime

class Item(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    order_id = database.Column(database.Integer, database.ForeignKey('order_details.id'))
    product_id = database.Column(database.Integer, database.ForeignKey('product.id'))
    quantity = database.Column(database.Integer)
    total = database.Column(database.Integer)
    timestamp = database.Column(database.DateTime)

    def __init__(self, order, product, quantity, total, timestamp=None):
        self.order_id = order.id
        self.product_id = product.id
        self.quantity = quantity
        self.total = total
        if timestamp is None:
            self.timestamp = datetime.utcnow()

    def __repr__(self):
        return self.order_id