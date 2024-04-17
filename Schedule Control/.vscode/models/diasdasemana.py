from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config import db

class DiasDaSemana(db.Model):
    __tablename__ = "DiasDaSemana"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(10), nullable= False)
    abreviacao = db.Column(db.String(5), nullable= False)
    numero = db.Column(db.Integer, nullable= False)
    id_cadastro = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable= False)
    ativacao = db.relationship('Horarios',secondary = "Ativacoes", lazy= "subquery", backref= db.backref("Horarios", lazy= True))


    
