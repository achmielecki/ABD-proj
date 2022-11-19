from flask import render_template, request
from app.models.Magazine import Magazine

ROWS_PER_PAGE = 20


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
