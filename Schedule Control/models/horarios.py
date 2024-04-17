from sqlalchemy import Column, Integer, String, ForeignKey
from config import db

class Horarios(db.Model):
    __tablename__ = "horario"

    id_horarios = db.Column(db.Integer, primary_key=True)
    dias_semana = db.Column(db.String(15))
    horas = db.Column(db.String(15))
    data_aula = db.Column(db.Date)
    id_oferta = db.Column(db.Integer, db.ForeignKey('oferta.id_oferta'))  # Corrija o nome da coluna de chave estrangeira
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    # cancelado_data = db.Column(db.Date)
    cancelado = db.Column(db.Boolean, default=False)
    
    disciplina = db.relationship('Disciplinas', back_populates='horarios')