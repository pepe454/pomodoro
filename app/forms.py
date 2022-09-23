from flask_wtf import FlaskForm
from wtforms import StringField, IntField, SubmitField


class PomodoroForm(FlaskForm):
    focus_timer = IntField("How long do you want to focus?", validators=validate_timer())
    break_timer = IntField("How long do you want to rest?", validators=validate_timer())
    rewards = StringField("What is something you do to relax?")
    submit == SubmitField("Start!")

