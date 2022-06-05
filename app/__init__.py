from glob import glob
from importlib import import_module

from flask import Blueprint, Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
ins_db = SQLAlchemy()

class Config:
    DEBUG = False
    SQLALCHEMY_POOL_TIMEOUT = 600
    SQLALCHEMY_POOL_RECYCLE1 = 300
    SQLALCHEMY_MAX_OVERFLOW = 10
class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + 'postgres' + ':' + 'Tiago2022' + '@' + 'localhost' + '/' + 'postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app(str_config_name):
    ins_app = Flask(__name__)
    ins_app.config.from_object(DevelopmentConfig)
    ins_db.init_app(ins_app)
    ins_app.register_blueprint(ins_blueprint)
    ins_app.app_context().push()
    return ins_app

ins_blueprint = Blueprint('api', __name__)

ins_api = Api(ins_blueprint,
              title='Seat availability detection',
              version='1.0.0',
              description='Back-end API for Seat availability detection',
              )

dct_namespaces = []
for controller in glob('**/api/*.py', recursive=True):
    if controller.endswith('__init__.py'):
        continue
    import os
    if os.name == "nt":
        str_module_path = '.'.join(controller[:-3].split('\\'))
    elif os.name == "posix":
        str_module_path = '.'.join(controller[:-3].split('/'))
    try:
        dct_auth = ins_api.authorizations
        ins_module = import_module(str_module_path)

        if os.name == "nt":
            ins_api.add_namespace(ins_module.ins_namespace,path ='/' +controller[:-3].split('\\')[2])
        elif os.name == "posix":
            ins_api.add_namespace(ins_module.ins_namespace,path ='/' +controller[:-3].split('/')[2])
        
    except Exception as str_error:
        print(str_error)
