from Shopacholic import database
from datetime import datetime

class OrderDetails(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    total = database.Column(database.Float)
    status = database.Column(database.String(30))
    timestamp = database.Column(database.DateTime)

    def __init__(self, total, status, timestamp=None):
        self.total = total
        self.status = status
        if timestamp is None:
            self.timestamp = datetime.utcnow()

    def __repr__(self):
        return self.id