from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

usuario_api = Blueprint('usuario_api', __name__)

class User(BaseModel):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(70), nullable=False)
    telefone = db.column(db.String(20))
    email = db.Column(db.String(70), unique=True, index=True)
    endereco = db.Column(db.String(100))


    def json(self):
        return {
            "nome":self.nome,
            "telefone":self.telefone,
            "email":self.email,
            "endereco":self.endereco
        }