from flask import Blueprint, request, jsonify
from app import db
from models import Usuario
from utils import hash_password, check_password, create_log
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")
    if not nome or not email or not senha:
        return jsonify({"msg": "nome, email e senha são obrigatórios"}), 400
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"msg": "email já cadastrado"}), 409
    u = Usuario(nome=nome, email=email, senha_hash=hash_password(senha))
    db.session.add(u)
    db.session.commit()
    create_log(f"Usuário registrado: {email}", usuario_id=u.id)
    return jsonify({"id": u.id, "email": u.email, "nome": u.nome}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    senha = data.get("senha")
    if not email or not senha:
        return jsonify({"msg": "email e senha são obrigatórios"}), 400
    user = Usuario.query.filter_by(email=email).first()
    if not user or not check_password(senha, user.senha_hash):
        return jsonify({"msg": "Credenciais inválidas"}), 401
    token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(hours=8))
    create_log(f"Usuário logou: {email}", usuario_id=user.id)
    return jsonify({"access_token": token}), 200

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = Usuario.query.get(user_id)
    if not user:
        return jsonify({"msg": "Usuário não encontrado"}), 404
    return jsonify({"id": user.id, "nome": user.nome, "email": user.email}), 200
