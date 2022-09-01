from flask import Blueprint

exp = Blueprint('exp', __name__, template_folder='templates', url_prefix='/exp')

from . import routes

