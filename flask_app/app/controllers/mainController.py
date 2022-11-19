from flask import render_template
from sqlalchemy import create_engine

engine = create_engine("postgresql://flaskapp:flaskapp@db:5432/flaskapp", echo=True)


def index():
    return render_template("index.html")

