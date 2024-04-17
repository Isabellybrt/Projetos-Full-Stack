from flask import Flask, jsonify, render_template, session, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy.inspection import inspect


app = Flask(__name__, template_folder= "templates", static_folder= "static")
user = 'user04'
password = quote_plus('ted@010203')
host = '139.144.26.210'
port = '3306'
database = 'db_equipe04'

connection_string = (f"mysql://{user}:{password}@{host}:{port}/{database}")
engine = create_engine(connection_string)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
db = SQLAlchemy(app)

app.secret_key = "user04"