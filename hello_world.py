from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
    return render_template("template.html", name=name)


@app.route("/jedi/<first>/<last>")
def jedi(first, last):
    return "your jedi name is: " + last[0:3] + first[0:2]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)