from time import sleep

from flask import flash, redirect, render_template

from app import app, forms


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = forms.PomodoroForm()

    if form.validate_on_submit():
        focus, brk = form.focus_timer.data, form.break_timer.data
        flash(f"Pomodoro timer requested with {focus} focus minutes and {brk} break minutes")
        return redirect('/timer')

    welcome = "Welcome to Pomodor Timer"
    return render_template("index.html", welcome=welcome, form=form)


@app.route("/timer")
def timer():
    return render_template("timers.html")
