from flask import Blueprint
from app.controllers.mainController import *
from app.controllers.magazineController import *

blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(index)

blueprint.route("/magazyny/", methods=["GET", "POST"])(magazines)
blueprint.route("/magazyny/<int:id>/", methods=["GET"])(magazine)
blueprint.route("/query1/", methods=["GET"])(query1)
# blueprint.route("/query1/orm", methods=["GET"])(query1orm)
# blueprint.route("/query1/sql", methods=["GET"])(query1sql)
blueprint.route("/query2/", methods=["GET"])(query2)
