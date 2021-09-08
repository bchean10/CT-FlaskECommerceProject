from flask import Blueprint

bp = Blueprint('product', __name__, url_prefix='/prod')

from . import routes, models