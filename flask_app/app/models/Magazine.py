from app.database.database import db


class Magazine(db.Model):
    __tablename__ = "Magazine"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    street = db.Column(db.String(50))
    postal_code = db.Column(db.String(10), unique=True)
    country = db.Column(db.String(100))
    workers = db.relationship("Worker", backref="magazine", lazy="dynamic")

    def __init__(self, city, street, postal_code, country, id=None):
        self.id = id
        self.city = city
        self.street = street
        self.postal_code = postal_code
        self.country = country
