from logging import debug
from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Pipe1709_'
app.config['MYSQL_DB']='Lacosteña'
mysql=MySQL(app)




@app.route("/")
def login():
    return render_template("login.html")


@app.route("/Registro")
def registro():
    return render_template("Registro.html")

@app.route("/Crear", methods=["POST"])
def create():
    if request.method == "POST":
        fullname = request.form['fullname']
        correo = request.form['correo']
        password = request.form['password']
        rptpassword=request.form['rptpassword']
        if rptpassword == password :
            cur= mysql.connection.cursor()
            cur.execute("INSERT INTO empleado (fullname,correo,password) VALUES (%s,%s,%s)",(fullname,correo,password))
            mysql.connection.commit()
            return redirect("/")
        else:
            return "Error grave"

@app.route("/home")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)