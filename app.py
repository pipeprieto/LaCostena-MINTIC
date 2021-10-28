from logging import debug
from flask import Flask, render_template,request,redirect,session   
# from flask_mysqldb import MySQL,MySQLdb
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
    if request.method == "GET":
        connection = mysql.connect()
        cur = connection.cursor()
        cur.execute("SELECT * FROM `empleado`")
        results = cur.fetchall()
        print(results)
        connection.commit()
        return render_template("login.html",results=results)


@app.route("/Registro")
def registro():
    return render_template('Registro.html')

@app.route("/Crear", methods=["GET","POST"])
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
                return redirect("/")
            else:
                return "Error grave"

@app.route("/home")
def index():
    if request.method == "GET":
        connection = mysql.connect()
        cur = connection.cursor()
        cur.execute("SELECT * FROM `empleado`")
        results = cur.fetchall()
        connection.commit()
        return render_template("index.html",results=results)


if __name__ == '__main__':
    app.run(port=8080, debug=True)