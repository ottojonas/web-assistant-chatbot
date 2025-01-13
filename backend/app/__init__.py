from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

def create_app(): 
    app = Flask(__name__)
    app.config[""] = ""
    app.config[""] = False 
    db.init_app(app)

    from .routes import routes 
    app.register_blueprint(routes, url_prefix = '/api')

    return app 
