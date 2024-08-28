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

@app.route("/register")
def register(name=None):
    return render_template('register.html')

@app.route("/login")
def login(name=None):
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)
