from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def helloWorld():
    return "Hello World!"


@app.route("/<name>")
def reply(name):
    return f"Hello, {escape(name)}!"

@app.route("/hello")
def hello():
    return render_template("hello.html")