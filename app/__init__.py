from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.usuario.models import usuario_api
from app.carrinho.models import carrinho_api
from app.carro.models import carro_api
from app.moto.models import moto_api
from app.cupom.models import cupom_api

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(usuario_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(carro_api)
    app.register_blueprint(moto_api)
    app.register_blueprint(cupom_api)


    return app
