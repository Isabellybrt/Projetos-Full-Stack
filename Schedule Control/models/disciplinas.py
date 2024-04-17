from sqlalchemy import Column, Integer, String
from config import db

class Disciplinas(db.Model):
    __tablename__ = "disciplina"

    id = db.Column(db.Integer, primary_key=True)
    carga_horaria = db.Column(db.String(255))
    nome = db.Column(db.String(255), nullable=False, unique=True)
    
    horarios = db.relationship('Horarios', back_populates='disciplina')
    
    turmas = db.relationship('Turmas', secondary="oferta", lazy='subquery', backref=db.backref('disciplinas', lazy=True))
