from flask import Flask, render_template, session
from db.db import Session
from core.config import settings
from flask_sqlalchemy import SQLAlchemy

from api.audits.audits import api_audits
from api.funcionality.funcionality import api_funcionality
from api.perfiles.perfiles import api_perfiles
from api.roles.roles import api_roles
from api.permisos.permisos import api_permisos
from api.usuario.usuario import api_usuario
from api.subfuncionalidad.subfuncionalidad import api_subfuncionalidad
from api.asigroles.asigroles import api_asigroles
from api.asigperfiles.asigperfiles import api_asigperfiles
from api.asigaccesos.asigaccesos import api_asigaccesos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "Th1s1ss3cr3t"

# BD
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# session_bd = Session()

app.register_blueprint(api_audits)
app.register_blueprint(api_funcionality)
app.register_blueprint(api_perfiles)
app.register_blueprint(api_roles)
app.register_blueprint(api_permisos)
app.register_blueprint(api_usuario)
app.register_blueprint(api_subfuncionalidad)
app.register_blueprint(api_asigroles)
app.register_blueprint(api_asigperfiles)
app.register_blueprint(api_asigaccesos)


@app.route("/health", methods=["GET"])
def Health_Check():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
