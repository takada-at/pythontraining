from flask import Flask
from .modules import hello
class Config:
    ENV = 'local'
    DEBUG = True
    DBAUTH = ''

def get_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + '.Config')
    app.register_blueprint(hello.module, url_prefix='')
    return app
