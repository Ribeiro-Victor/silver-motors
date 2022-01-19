from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

carrinho_api = Blueprint('carrinho_api', __name__)

class Carrinho(BaseModel):

    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precoTotal = db.Column(db.Float, default = 0.0)
    quantidadeProdutos = db.Column(db.Integer)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref=db.backref("carrinho", uselist=False))

    def json(self):
        return {
            "preco total":self.precoTotal,
            "quantidade de produtos":self.quantidadeProdutos
        }