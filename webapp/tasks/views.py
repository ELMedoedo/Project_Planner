
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import logout_user
from webapp.user.views import blueprint as user_blueprint


blueprint = Blueprint("planner", __name__, url_prefix="/planner")


@blueprint.route("/planner")
def planner():
    return render_template("planner/planner.html")


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы")
    return redirect(url_for("user.login"))

