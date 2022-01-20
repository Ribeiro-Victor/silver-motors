from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

cupom_api = Blueprint('cupom_api', __name__)


class Cupom(BaseModel):

    __tablename__ = 'cupom'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descontoPercentual = db.Column(db.Float)
    paraCarro = db.Column(db.Boolean)
    paraMoto = db.Column(db.Boolean)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref=db.backref("cupom", uselist=False))

    def json(self):
        return {
            "desconto percentual":self.descontoPercentual,
            "para carro":self.paraCarro,
            "para moto":self.paraMoto
        }