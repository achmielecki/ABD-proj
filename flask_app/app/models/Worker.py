from app.database.database import db
from app.models.Person import Person


class Worker(Person):
    __tablename__ = "Worker"

    shift = db.Column(db.String(128))

    def __init__(self, name, surname, email, salary, shift, magazine_id, id=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary
        self.shift = shift
        self.magazine_id = magazine_id
