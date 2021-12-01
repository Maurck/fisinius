'''
config.py: modulo donde se configura la aplicación
'''
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from mongoengine import connect

def load_enviromental_variables():
    try:
        load_dotenv()
    except:
        print("No se cargó el .env")

def get_stage():
    return os.getenv('STAGE', 'DEVELOPMENT')

def server_config(app):
    load_enviromental_variables()
    cors_config(app)
    database_config()
    app.config['JSON_AS_ASCII'] = False

def cors_config(app):
    CORS(app=app)

def database_config():
    DB_URI = os.getenv('DB_URI', '')
    connect(host=DB_URI)

def get_app(__name__):
    app = Flask(__name__)
    return app

def run_app(app):

    STAGE = get_stage()

    if STAGE == 'DEVELOPMENT':
        app.run(debug=True, host='0.0.0.0', port=5000)
    elif STAGE == 'PRODUCTION':
        app.run(debug=False)
    
