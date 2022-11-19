from app.database.database import db
from app.models.Person import Person


class Director(Person):
    __tablename__ = "Director"

    def __init__(self, name, surname, email, salary, magazine_id, id=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary
        self.magazine_id = magazine_id
