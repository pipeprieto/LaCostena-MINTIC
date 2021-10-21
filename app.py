from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/Registro")
def registro():
    return render_template("Registro.html")

@app.route("/home")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)