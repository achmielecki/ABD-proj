from app import app
from flask import Flask
from flask_migrate import Migrate
from app.database.database import db
from app.routes.routes import blueprint
from app.models.Worker import Worker
from app.models.Magazine import Magazine
from app.models.Director import Director
import pandas as pd


def create_db_schema():
    with app.app_context():
        db.drop_all()
    with app.app_context():
        db.create_all()
        db.session.commit()


def load_generated_data():
    magazines_csv = pd.read_csv(r"./sample_data/magazines.csv", delimiter=r",", encoding='utf-16')
    magazines_df = pd.DataFrame(magazines_csv, columns=["id", "city", "street", "postal_code", "country"])
    workers_csv = pd.read_csv(r"./sample_data/workers.csv", delimiter=",", encoding='utf-16')
    workers_csv_df = pd.DataFrame(workers_csv,
                                  columns=["id", "name", "surname", "email", "salary", "shift", "magazine_id"])
    directors_csv = pd.read_csv(r"./sample_data/directors.csv", delimiter=",", encoding='utf-16')
    directors_df = pd.DataFrame(directors_csv, columns=["id", "name", "surname", "email", "salary", "magazine_id"])

    with app.app_context():
        for index, row in magazines_df.iterrows():
            db.session.add(
                Magazine(
                    id=row["id"],
                    city=row["city"],
                    street=row["street"],
                    postal_code=row["postal_code"],
                    country=row["country"]
                )
            )
        db.session.commit()

    with app.app_context():
        for index, row in workers_csv_df.iterrows():
            db.session.add(
                Worker(
                    id=row["id"],
                    name=row["name"],
                    surname=row["surname"],
                    email=row["email"],
                    salary=row["salary"],
                    shift=row["shift"],
                    magazine_id=row["magazine_id"]
                )
            )
        db.session.commit()

    with app.app_context():
        for index, row in directors_df.iterrows():
            db.session.add(
                Director(
                    id=row["id"],
                    name=row["name"],
                    surname=row["surname"],
                    email=row["email"],
                    salary=row["salary"],
                    magazine_id=row["magazine_id"]
                )
            )
        db.session.commit()
    with app.app_context():
        db.session.commit()


app = Flask(__name__, template_folder="app/templates")
app.config.from_object("app.config.Config")
db.init_app(app)
app.register_blueprint(blueprint, url_prefix="/")
migrate = Migrate(app, db)
create_db_schema()
load_generated_data()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
