from flask import Flask
from app import create_app
from flask_restplus import Api, Resource

APP = create_app("Development")

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(host='0.0.0.0',debug=True)
