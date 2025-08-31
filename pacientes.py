from flask import Blueprint, request, jsonify
from app import db
from models import Paciente
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils import create_log

pacientes_bp = Blueprint("pacientes", __name__)

@pacientes_bp.route("/pacientes", methods=["POST"])
@jwt_required()
def criar_paciente():
    data = request.get_json() or {}
    nome = data.get("nome")
    cpf = data.get("cpf")
    contato = data.get("contato")
    historico = data.get("historico_clinico")
    if not nome or not cpf:
        return jsonify({"msg": "nome e cpf são obrigatórios"}), 400
    if Paciente.query.filter_by(cpf=cpf).first():
        return jsonify({"msg": "paciente com esse CPF já existe"}), 409
    p = Paciente(nome=nome, cpf=cpf, contato=contato, historico_clinico=historico)
    db.session.add(p)
    db.session.commit()
    create_log(f"Paciente criado: {p.nome} (CPF: {p.cpf})", usuario_id=get_jwt_identity())
    return jsonify({"id": p.id, "nome": p.nome, "cpf": p.cpf}), 201

@pacientes_bp.route("/pacientes", methods=["GET"])
@jwt_required()
def listar_pacientes():
    pacientes = Paciente.query.order_by(Paciente.nome).all()
    return jsonify([{"id": p.id, "nome": p.nome, "cpf": p.cpf, "contato": p.contato} for p in pacientes]), 200

@pacientes_bp.route("/pacientes/<int:paciente_id>", methods=["GET"])
@jwt_required()
def recuperar_paciente(paciente_id):
    p = Paciente.query.get_or_404(paciente_id)
    return jsonify({"id": p.id, "nome": p.nome, "cpf": p.cpf, "contato": p.contato, "historico_clinico": p.historico_clinico}), 200

@pacientes_bp.route("/pacientes/<int:paciente_id>", methods=["PUT"])
@jwt_required()
def atualizar_paciente(paciente_id):
    p = Paciente.query.get_or_404(paciente_id)
    data = request.get_json() or {}
    p.nome = data.get("nome", p.nome)
    p.cpf = data.get("cpf", p.cpf)
    p.contato = data.get("contato", p.contato)
    p.historico_clinico = data.get("historico_clinico", p.historico_clinico)
    db.session.commit()
    create_log(f"Paciente atualizado: {p.id}", usuario_id=get_jwt_identity())
    return jsonify({"msg": "Paciente atualizado com sucesso"}), 200

@pacientes_bp.route("/pacientes/<int:paciente_id>", methods=["DELETE"])
@jwt_required()
def deletar_paciente(paciente_id):
    p = Paciente.query.get_or_404(paciente_id)
    db.session.delete(p)
    db.session.commit()
    create_log(f"Paciente deletado: {paciente_id}", usuario_id=get_jwt_identity())
    return jsonify({"msg": "Paciente excluído"}), 200
