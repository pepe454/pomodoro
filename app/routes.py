from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    title = "Pomodoro Timer"
    welcome = "Welcome to Pomodor Timer"
    return render_template("index.html", title=title, welcome=welcome)

