from sqlalchemy import Column, Integer, String
from config import db

class Turmas(db.Model):
    __tablename__ = "turma"

    id = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.String(15), nullable=False)
    turno = db.Column(db.String(20), nullable=False)
    
    __table_args__=(
        db.UniqueConstraint('curso', 'ano', 'turno', name='dados_turma_unico'),
    )

    def __repr__(self):
        return f'<Turmas {self.curso}, {self.ano}>'
