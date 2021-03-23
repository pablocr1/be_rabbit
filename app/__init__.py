from flask import Flask
from app.services.extensions import db, jwt, cors, cache

def create_app():
    #app
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # extension
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)


    return app