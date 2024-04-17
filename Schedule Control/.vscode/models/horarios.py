from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config import db

class Horarios(db.Model):
    __tablename__ = "Horarios"

    id = db.Column(db.Integer, primary_key = True)
    hora = db.Column(db.Integer, nullable= False)
    minuto = db.Column(db.Integer, nullable= False)
    id_cadastro = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable= False)
    
    