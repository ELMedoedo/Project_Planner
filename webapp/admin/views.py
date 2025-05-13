from flask import Blueprint
from flask_login import login_required, current_user



blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("/")
@login_required
def admin_index():
    if current_user.is_admin:
        return ("Привет админ")
    else:
        return ("Тебе сюда нельзя")