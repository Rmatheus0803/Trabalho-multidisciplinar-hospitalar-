from app import app, db
from models import Usuario
from utils import hash_password
from dotenv import load_dotenv
load_dotenv()

def create_all():
    with app.app_context():
        print("Criando tabelas...")
        db.create_all()
        print("Tabelas criadas.")

def seed_admin(nome="admin", email="admin@localhost", senha="admin123"):
    with app.app_context():
        if Usuario.query.filter_by(email=email).first():
            print("Admin já existe.")
            return
        u = Usuario(nome=nome, email=email, senha_hash=hash_password(senha))
        db.session.add(u)
        db.session.commit()
        print(f"Admin criado: {email} / {senha}")

if __name__ == "__main__":
    create_all()
    seed_admin()
