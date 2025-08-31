from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    logs = db.relationship("Log", backref="usuario", lazy=True)

class Paciente(db.Model):
    __tablename__ = "paciente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    contato = db.Column(db.String(30))
    historico_clinico = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

class Log(db.Model):
    __tablename__ = "log"
    id = db.Column(db.Integer, primary_key=True)
    operacao = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=True)
