from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# importar modelos e rotas (evitar circular import)
import models  # noqa: F401
from routes.auth import auth_bp
from routes.pacientes import pacientes_bp

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(pacientes_bp, url_prefix="/api")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
