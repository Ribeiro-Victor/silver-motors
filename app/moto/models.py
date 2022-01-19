from app.extensions import db
from app.models import BaseModel

class Moto(BaseModel):

    __tablename__ = 'moto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, default = 0.0)
    montadora = db.Column(db.String(25))
    modelo = db.Column(db.String(25))
    ano = db.Column(db.Integer)
    quilometragem = db.Column(db.Float)
    cor = db.Column(db.String(20))

    def json(self):
        return {

        }