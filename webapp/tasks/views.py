
from flask import Blueprint, render_template, flash, redirect, url_for, request, session
from flask_login import logout_user, current_user
from datetime import datetime

from webapp.static.enums import ActionType, ObjectType
from webapp.tasks.models import Dashboard, Task
from webapp.tasks.forms import TaskForm
from webapp.db import db


blueprint = Blueprint("planner", __name__, url_prefix="/planner")


@blueprint.route("/planner")
def planner():
    # Получаем все доски пользователя
    dashboards = Dashboard.query.filter_by(user_id=current_user.id).order_by(Dashboard.id).all()
    
    # Автоматическое создание основной доски при отсутствии
    if not dashboards:
        new_dashboard = Dashboard(
            user_id=current_user.id,
            user_name=current_user.user,
            table_type="Основная",
            table_comment="Моя основная доска задач"
        )
        db.session.add(new_dashboard)
        db.session.commit()
        dashboards = [new_dashboard]

    # Получаем текущую доску из сессии или первую
    current_dashboard_id = session.get('current_dashboard_id', dashboards[0].id)
    dashboard = next((d for d in dashboards if d.id == current_dashboard_id), dashboards[0])
    
    # Определяем соседние доски
    current_index = dashboards.index(dashboard)
    prev_dashboard = dashboards[current_index-1] if current_index > 0 else None
    next_dashboard = dashboards[current_index+1] if current_index < len(dashboards)-1 else None
    
    return render_template(
        "planner/planner.html",
        dashboard=dashboard,
        tasks=Task.query.filter_by(dashboard_id=dashboard.id).order_by(Task.id).all(),
        task_form=TaskForm(),
        prev_dashboard=prev_dashboard,
        next_dashboard=next_dashboard
    )


@blueprint.route("/create_dashboard", methods=["POST"])
def create_dashboard():
    new_dashboard = Dashboard(
        user_id=current_user.id,
        user_name=current_user.user,
        table_type="Новая доска",
        table_comment=f"Доска от {datetime.now().strftime('%d.%m.%Y')}"
    )
    db.session.add(new_dashboard)
    db.session.commit()

    # log_action(
    #         user_id=current_user.id,
    #         action=ActionType.CREATE,
    #         object_type=ObjectType.DASHBOARD,
    #         object_id=new_dashboard.id,
    #         details=f"Created dashboard: {new_dashboard.table_comment}"
    #     )
    
    
    session['current_dashboard_id'] = new_dashboard.id
    return redirect(url_for('planner.planner'))


@blueprint.route("/prev_dashboard")
def prev_dashboard():
    dashboards = Dashboard.query.filter_by(user_id=current_user.id).order_by(Dashboard.id).all()
    current_id = session.get('current_dashboard_id', dashboards[0].id)
    
    for i, d in enumerate(dashboards):
        if d.id == current_id and i > 0:
            session['current_dashboard_id'] = dashboards[i-1].id
            break
            
    return redirect(url_for('planner.planner'))

@blueprint.route("/next_dashboard")
def next_dashboard():
    dashboards = Dashboard.query.filter_by(user_id=current_user.id).order_by(Dashboard.id).all()
    current_id = session.get('current_dashboard_id', dashboards[0].id)
    
    for i, d in enumerate(dashboards):
        if d.id == current_id and i < len(dashboards)-1:
            session['current_dashboard_id'] = dashboards[i+1].id
            break
            
    return redirect(url_for('planner.planner'))

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


@blueprint.route("/delete_dashboard", methods=["POST"])
def delete_dashboard():
    dashboard_id = request.form.get("dashboard_id")

    try:
        dashboard = Dashboard.query.get(dashboard_id)
        
        if not dashboard:
            flash("Доска не найдена", "danger")
            return redirect(url_for('planner.planner'))
            
        if dashboard.user_id != current_user.id:
            flash("Доступ запрещён", "danger")
            return redirect(url_for('planner.planner'))

        # Запрет удаления основной доски
        if dashboard.table_type == "Основная":
            flash("Нельзя удалить основную доску", "danger")
            return redirect(url_for('planner.planner'))

        db.session.delete(dashboard)
        db.session.commit()
        flash("Доска успешно удалена", "success")

        # Автоматическое создание основной доски при удалении последней
        remaining = Dashboard.query.filter_by(user_id=current_user.id).count()
        if remaining == 0:
            new_dashboard = Dashboard(
                user_id=current_user.id,
                user_name=current_user.user,
                table_type="Основная",
                table_comment="Моя основная доска задач"
            )
            db.session.add(new_dashboard)
            db.session.commit()
            session['current_dashboard_id'] = new_dashboard.id

    except Exception as e:
        db.session.rollback()
        flash(f"Ошибка: {str(e)}", "danger")
    
    return redirect(url_for('planner.planner'))





@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы вышли из системы")
    return redirect(url_for("user.login"))


