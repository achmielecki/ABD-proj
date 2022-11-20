import os


class Config(object):
    SECRET_KEY = "SECRET"

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://flaskapp:flaskapp@localhost:5432/flaskapp")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
