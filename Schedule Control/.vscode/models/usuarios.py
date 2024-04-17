from sqlalchemy import Column, Integer, String
from config import db

class Usuarios(db.Model):
    __tablename__ = "Usuarios"

    id = db.Column(db.Integer, primary_key = True)
    matricula = db.Column(db.String(30), nullable= False, unique= True)
    email = db.Column(db.String(120), unique= True, nullable= False)
    senha = db.Column(db.String(200), nullable= False)
    horarios_cadastrados = db.relationship('Horarios', backref= 'id_usuario', lazy = True)
    dia_semana_cadastrados = db.relationship('DiasDaSemana', backref= 'id_diadasemana', lazy = True)

