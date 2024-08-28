from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import bcrypt


app = Flask(__name__)
DATABASE_URL = "postgresql+psycopg2://postgres:prueba123@localhost/web"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


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

if __name__ == "__main__":
    app.run(debug=True)
