from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#---------------------------------------------------------
# init SQLAlchemy so we can use it later in our models
#---------------------------------------------------------
db = SQLAlchemy()

#---------------------------------------------------------
# init a LoginManager so we can use it later
#---------------------------------------------------------
login_manager = LoginManager()

##########################################################
# function to create, configure and return the Flask app
##########################################################
def create_app():

    app = Flask(__name__)

    __config(app)
    __config_db(app)
    __config_lm(app)
    __register_bp(app)

    return app

##########################################################
# function to configure the Flask app
##########################################################
def __config(app):

    #configure the flask app
    # TODO: use the config module here
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # disable SQLAlchemy's eventing system
    # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

##########################################################
# function to init the database
##########################################################
def __config_db(app):

    # before creating db schema and tables, push the app context.
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts
    app.app_context().push()

    # first, import the db models
    from .auth import models
    from .exp import models
    
    # initialize the database
    db.init_app(app)

    # create schema and tables "if not exist"
    db.create_all()

##########################################################
# function to configure the login manager
##########################################################
def __config_lm(app):

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

##########################################################
# function to register all blueprints 
#
# Note: import blueprints here to avoid app initialization
#       errors when you place imports at the top
##########################################################
def __register_bp(app):

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for expenses
    from .exp import exp as exp_blueprint
    app.register_blueprint(exp_blueprint)

