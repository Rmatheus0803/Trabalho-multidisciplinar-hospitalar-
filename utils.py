import bcrypt
from app import db
from models import Log

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

def create_log(operacao: str, usuario_id: int = None):
    l = Log(operacao=operacao, usuario_id=usuario_id)
    db.session.add(l)
    db.session.commit()
