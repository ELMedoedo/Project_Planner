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

    due_date = DateField(
        "Срок выполнения",
        validators=[DataRequired()],
        render_kw={"class": "form-control", "min": datetime.now().strftime("%d-%m-%Y")},
    )


