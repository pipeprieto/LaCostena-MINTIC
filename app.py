from logging import debug
from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql=MySQL()


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Pipe1709_'
app.config['MYSQL_DATABASE_DB']='lacosteña'
mysql.init_app(app)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/Registro")
def registro():
    return render_template("Registro.html")

@app.route("/Crear", methods=["POST"])
def create():
    if request.method == "POST":
        name = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        rptpassword=request.form['rptpassword']
        if rptpassword == password :
            connection= mysql.connect()
            cur = connection.cursor()
            cur.execute("INSERT INTO empleado (nombre,correo,contraseña) VALUES (%s,%s,%s)",(name,correo,password))
            connection.commit()
            results = cur.fetchall()
            return redirect("/")
        else:
            return "Error grave"

@app.route("/home")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)