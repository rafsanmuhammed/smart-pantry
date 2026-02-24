from  flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

class PantryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    barcode = db.Column(db.String(50), nullable=True)
    expiry_date = db.Column(db.Date, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'barcode': self.barcode,
            'expiry_date': self.expiry_date.strftime('%Y-%m-%d'),
            'days_left': (self.expiry_date - datetime.utcnow().date()).days
        } 
    

    