from flask import render_template, request
import time
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.models.Worker import Worker
from app.models.Magazine import Magazine
from app.models.Director import Director
import sqlalchemy as db
from sqlalchemy.sql import func
from sqlalchemy import desc

ROWS_PER_PAGE = 20
engine = create_engine("postgresql://flaskapp:flaskapp@localhost:5432/flaskapp", echo=True)


def magazines():
    if request.method == "POST":
        return None
    else:
        page = request.args.get("page", 1, type=int)
        magazines = Magazine.query.paginate(page=page, per_page=ROWS_PER_PAGE)

        return render_template("magazines.html", magazines=magazines)


def magazine(id):
    magazine = Magazine.query.get_or_404(id)
    return render_template("magazine.html", magazine=magazine)


def query1():
    with Session(engine) as session:
        resetSalaries()
        session.expire_all()
        start_time = time.time()
        director = \
            session.query(Director).filter(Director.name == "Sylwia").filter(Director.surname == "Mikołaj").all()[0]
        count = session.query(Worker).filter(Worker.salary < 4000).filter(
            Worker.magazine_id == director.magazine_id).update(
            {"salary": 4000})
        session.commit()
        orm_time = time.time() - start_time

        resetSalaries()
        session.expire_all()
        start_time = time.time()
        session.execute(
            'UPDATE \"Worker\" SET salary = 4000 WHERE salary < 4000 AND magazine_id = \
            (select magazine_id from \"Director\" where name = \'Sylwia\' AND surname = \'Mikołaj\')'
            )
        session.commit()
        sql_time = time.time() - start_time

        return render_template("query1.html", count=count, orm_time=orm_time, sql_time=sql_time)


def query1orm():
    with Session(engine) as session:
        start_time = time.time()
        director = \
            session.query(Director).filter(Director.name == "Sylwia").filter(Director.surname == "Mikołaj").all()[0]
        count = session.query(Worker).filter(Worker.salary < 4000).filter(
            Worker.magazine_id == director.magazine_id).update(
            {"salary": 4000})
        session.commit()
        orm_time = time.time() - start_time

        resetSalaries()
        return render_template("query1orm.html", count=count, orm_time=orm_time)


def resetSalaries():
    with Session(engine) as session:
        session.execute('UPDATE \"Worker\" SET salary = 2000 WHERE salary = 4000 AND magazine_id = 10')
        session.commit()


def query1sql():
    with Session(engine) as session:
        start_time = time.time()
        session.execute('UPDATE \"Worker\" SET salary = 4000 WHERE salary < 4000 AND magazine_id = 10')
        session.commit()
        sql_time = time.time() - start_time

        resetSalaries()
        return render_template("query1sql.html", sql_time=sql_time)


def query2():
    with Session(engine) as session:
        session.expire_all()
        start_time = time.time()
        magazines = session\
            .query(Magazine.id, func.sum(Worker.salary).label('sum'), Magazine.city, Director.name, Director.surname)\
            .join(Worker)\
            .join(Director)\
            .group_by(Magazine.id, Magazine.city, Director.name, Director.surname)\
            .order_by(desc('sum'))\
            .all()

        orm_time = time.time() - start_time
        session.expire_all()
        start_time = time.time()
        magazines2 = session.execute(
            'SELECT "Magazine".id, sum(W.salary) AS sum, "Magazine".city, D.name, D.surname \
            FROM "Magazine" \
            LEFT JOIN "Worker" W ON "Magazine".id = W.magazine_id \
            LEFT JOIN "Director" D on "Magazine".id = D.magazine_id \
            GROUP BY "Magazine".id, city, D.name, D.surname \
            ORDER BY sum DESC;'
        ).all()
        sql_time = time.time() - start_time

        return render_template("query2.html", orm_time=orm_time, sql_time=sql_time)
