from time import sleep

from flask import flash, redirect, render_template

from app import app, forms


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    title = "Pomodoro Timer"
    welcome = "Welcome to Pomodor Timer"
    form = forms.PomodoroForm()

    if form.validate_on_submit():
        focus, brk = form.focus_timer.data, form.break_timer.data
        flash(f"Pomodoro timer requested with {focus} focus minutes and {brk} break minutes")
        return redirect('/timer')

    return render_template("index.html", title=title, welcome=welcome, form=form)


@app.route("/timer")
def timer():
    return "Timer page is a work in progress!"
