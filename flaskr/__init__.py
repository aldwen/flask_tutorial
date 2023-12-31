import os
from flask import Flas.keys()

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.format_map(test_config)