
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import logout_user, current_user

from webapp.tasks.models import Dashboard, Task
from webapp.tasks.forms import TaskForm
from webapp.db import db


blueprint = Blueprint("planner", __name__, url_prefix="/planner")


@blueprint.route("/planner")
def planner():
    # Получаем первую доску текущего пользователя
    dashboard = Dashboard.query.filter_by(user_id=current_user.id).first()
    form = TaskForm()

    # task_form = TaskForm()

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
    tasks = Task.query.filter_by(dashboard_id=dashboard.id).order_by(Task.id).all()


    return render_template(
        "planner/planner.html",
        dashboard=dashboard,
        tasks=tasks,
        task_form=form
    )

@blueprint.route("/process_make_task", methods=["POST"])
def process_make_task():
    task_form = TaskForm()
    dashboard = Dashboard.query.filter_by(user_id=current_user.id).first()

    if not dashboard:
        flash("Сначала создайте доску")
        return redirect(url_for("planner.planner"))

    if task_form.validate_on_submit():
        try:
            new_task = Task(
                title=task_form.title.data,
                body=task_form.body.data,
                due_date=task_form.due_date.data,
                status=request.form.get("status"),
                dashboard_id=dashboard.id
            )
            
            db.session.add(new_task)
            db.session.commit()
            flash("Задача успешно создана")
        except Exception as e:
            db.session.rollback()
            flash(f"Ошибка: {str(e)}")
    
    else:
        for field, errors in task_form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле {getattr(task_form, field).label.text}: {error}")
    
    return redirect(url_for("planner.planner"))

@blueprint.route("/update_task_status", methods=["POST"])
def update_task_status():
    task_id = request.form.get('task_id')
    new_status = request.form.get('new_status')

    if not task_id or not new_status:
        flash("Недостаточно данных", "danger")
        return redirect(url_for('planner.planner'))

    try:
        task = db.session.get(Task, task_id)  
        if not task:
            flash("Задача не найдена", "danger")
            return redirect(url_for('planner.planner'))
        
        # Проверка через явное отношение
        if task.dashboard.user_id != current_user.id:
            flash("Доступ запрещён", "danger")
            return redirect(url_for('planner.planner'))

        task.status = new_status
        db.session.commit()
        flash("Статус обновлен", "success")
    
    except Exception as e:
        db.session.rollback()
        flash(f"Ошибка: {str(e)}", "danger")
    
    return redirect(url_for('planner.planner'))


@blueprint.route("/delete_task", methods=["POST"])
def delete_task():
    task_id = request.form.get("task_id")

    try: 
        task = Task.query.get(task_id)

        if not task_id or not task_id.isdigit():
            flash("Некорректный ID задачи", "danger")
            return redirect(url_for('planner.planner'))
        
        db.session.delete(task)
        db.session.commit()
        flash("Задача удалена", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Ошибка: {str(e)}", "danger")

    return redirect(url_for('planner.planner'))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы")
    return redirect(url_for("user.login"))


