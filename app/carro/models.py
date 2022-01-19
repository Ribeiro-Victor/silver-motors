from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

carro_api = Blueprint('carro_api', __name__)

class Carro(BaseModel):

    __tablename__ = 'carro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, default = 0.0)
    montadora = db.Column(db.String(25))
    modelo = db.Column(db.String(25))
    ano = db.Column(db.Date)
    quilometragem = db.Column(db.Float)
    cor = db.Column(db.String(20))

    def json(self):
        return {
            "montadora":self.montadora,
            "modelo":self.modelo,
            "ano":self.ano,
            "quilometragem":self.quilometragem,
            "cor":self.cor
        }