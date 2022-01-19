from app.extensions import db
from app.models import BaseModel

class Cupom(BaseModel):

    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descontoPercentual = db.Column(db.Float)
    paraCarro = db.Column(db.Boolean)
    paraMoto = db.Column(db.Boolean)


    def json(self):
        return {

        }