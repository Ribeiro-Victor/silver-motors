from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

item_api = Blueprint('item_api', __name__)

class Item(BaseModel):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    carrinho = db.relationship("Carrinho", backref=db.backref("item", uselist=False))
    id_carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    carro = db.relationship("Carro", backref=db.backref("item", uselist=False))
    id_moto = db.Column(db.Integer, db.ForeignKey('moto.id'))
    moto = db.relationship("Moto", backref=db.backref("item", uselist=False))

    def json(self):
        return {
            "quantidade":self.quantidade,
            "preco":self.preco,
            "id_carro":self.carro,
            "id_moto":self.moto,
            "id_carrinho":self.carrinho
        }