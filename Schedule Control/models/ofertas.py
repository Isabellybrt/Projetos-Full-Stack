from sqlalchemy import Column, Integer, ForeignKey
from config import db
from models.horarios import Horarios

class Ofertas(db.Model):
    __tablename__ = "oferta"

    id_oferta = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, db.ForeignKey("disciplina.id"))
    id_turma = db.Column(db.Integer, db.ForeignKey("turma.id"))
    id_professor = db.Column(db.Integer, db.ForeignKey("usuario.id_professor"))

    disciplina = db.relationship('Disciplinas', backref='ofertas', foreign_keys=[id_disciplina],
                                 primaryjoin='Ofertas.id_disciplina == Disciplinas.id')
    turma = db.relationship('Turmas', backref='ofertas', foreign_keys=[id_turma])
    horarios = db.relationship('Horarios', backref='ofertas', foreign_keys=[Horarios.id_oferta])
