from app.database.database import db
from sqlalchemy.orm import declared_attr


class Person(db.Model):
    __tablename__ = "Person"
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    salary = db.Column(db.Integer)

    @declared_attr
    def magazine_id(self):
        return db.Column(db.Integer, db.ForeignKey("Magazine.id"))
