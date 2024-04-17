from sqlalchemy import Column, Integer, String
from config import db

#Base = declarative_base()

class Usuarios(db.Model):
    __tablename__ = "usuario"

    id_professor = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(15), nullable=False)
    materias = db.Column(db.String(30), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)