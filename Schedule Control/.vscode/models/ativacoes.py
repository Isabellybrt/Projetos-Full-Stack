from sqlalchemy import Column, Integer, ForeignKey
from config import db

class Ativacoes(db.Model):
    __tablename__ = "Ativacoes"

    id_horario = db.Column("Horario",db.Integer, db.ForeignKey('Horarios.id'), nullable= False, primary_key= True)
    id_semana = db.Column("DiasDaSemana",db.Integer, db.ForeignKey('DiasDaSemana.id'), nullable=False, primary_key= True)
