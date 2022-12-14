from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


def validate_timer(form, field):
    if field.data > 60 or field.data < 1:
        raise ValidationError("timer must be between 1 and 60 minutes")


def validate_reward(form, field):
    if len(field.data) < 1:
        raise ValidationError("please enter something to do during the break")


class PomodoroForm(FlaskForm):
    focus_timer = IntegerField(
        "How long do you want to focus? (minutes)", validators=[validate_timer, DataRequired()]
    )
    break_timer = IntegerField(
        "How long do you want to rest?", validators=[validate_timer, DataRequired()]
    )
    rewards = StringField(
        "What is something you do to relax?", validators=[validate_reward, DataRequired()]
    )
    submit = SubmitField("Start!")

