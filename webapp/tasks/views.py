
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import logout_user, current_user
from webapp.user.views import blueprint as user_blueprint
from webapp.tasks.models import Dashboard, Task
from webapp.tasks.forms import TaskForm
from webapp.db import db
from datetime import datetime


blueprint = Blueprint("planner", __name__, url_prefix="/planner")


@blueprint.route("/planner")
def planner():
    # Получаем первую доску текущего пользователя
    dashboard = Dashboard.query.filter_by(user_id=current_user.id).first()
    form = TaskForm()
    
    if not dashboard:
        # Создаем новую доску если не существует
        dashboard = Dashboard(
            user_id=current_user.id,
            user_name=current_user.user,
            table_type="Основная",
            table_comment="Моя основная доска задач",
        )
        db.session.add(dashboard)
        db.session.commit()

    # Получаем задачи для этой доски
    tasks = Task.query.filter_by(dashboard_id=dashboard.id).all()
    
    return render_template(
        "planner/planner.html",
        dashboard=dashboard,
        tasks=tasks,
        form=form
    )

@blueprint.route("/process_make_task", methods=["POST"])
def process_make_task():
    form = TaskForm()
    dashboard = Dashboard.query.filter_by(user_id=current_user.id).first()

    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            body=form.body.data,
            status="Новая",
            due_date=form.due_date.data,
            dashboard_id=dashboard.id  # Добавляем связь с доской
        )
        
        db.session.add(new_task)
        db.session.commit()


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы")
    return redirect(url_for("user.login"))


