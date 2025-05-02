from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    SubmitField,
    BooleanField,
    DateField,
    HiddenField
)
from wtforms.validators import DataRequired, Length
from datetime import datetime


class DashboardForm(FlaskForm):
    table_type = StringField(
        "Тип доски",
        validators=[DataRequired(), Length(max=50)],
        render_kw={"class": "form-control"},
    )
    table_comment = TextAreaField(
        "Комментарий к доске",
        validators=[Length(max=500)],
        render_kw={
            "class": "form-control",
            "rows": 3,
        },
    )
    submit = SubmitField("Сохранить доску", render_kw={"class": "btn btn-primary"})


class TaskForm(FlaskForm):
    title = StringField(
        "Название задачи",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"class": "form-control"},
    )
    body = TextAreaField(
        "Описание задачи",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "rows": 4,
        },
    )
    # status = SelectField(
    #     "Статус задачи",
    #     choices=[
    #         ("Новая", "Новая"),
    #         ("В работе", "В работе"),
    #         ("Выполнено", "Выполнено"),
    #     ],
    #     validators=[DataRequired()],
    #     render_kw={"class": "form-select"},
    # )

    due_date = DateField(
        "Срок выполнения",
        validators=[DataRequired()],
        render_kw={"class": "form-control", "min": datetime.now().strftime("%d-%m-%Y")},
    )
    # submit = SubmitField("Сохранить задачу", render_kw={"class": "btn btn-success"})


# class TaskStatusForm(FlaskForm):
#     new_status = SelectField(
#         "Статус",
#         choices=[
#             ("Новая", "Новая"),
#             ("В работе", "В работе"),
#             ("Выполнено", "Выполнено"),
#         ],
#         validators=[DataRequired()],
#         render_kw={"class": "form-select"}
#     )
#     task_id = HiddenField("Task ID", validators=[DataRequired()])