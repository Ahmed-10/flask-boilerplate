from flask import Blueprint
import api.routes.category as category


api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(category.category_api)