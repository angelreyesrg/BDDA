from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Base de datos-----------------------------------------------------------------
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

app.config['SQLALCHEMY_BINDS'] = {
    'postgres': 'postgresql://postgres:1234@localhost:5432/postgres',
}

db = SQLAlchemy(app)

#Rutas--------------------------------------------------------------------------
@app.route("/")
def index(name=None):
    return render_template('index.html')

@app.route("/crear")
def crear(name=None):
    return render_template('crear.html')

@app.route("/consultar")
def consultar(name=None):
    return render_template('consultar.html')

@app.route("/actualizar")
def actualizar(name=None):
    return render_template('actualizar.html')

@app.route("/borrar")
def borrar(name=None):
    return render_template('borrar.html')


#Inicializar el servidor -------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
    