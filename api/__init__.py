from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from api.models import db
import api.routes as bp


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    def index():
        return 'Hello, World!'
    
    def http_error_handler(error):
        return jsonify({
            'name': error.name,
            'code': error.code,
            'description': error.description
        }), error.code

    app.add_url_rule('/', 'index', index)
    app.register_blueprint(bp.api)
    app.register_error_handler(HTTPException, http_error_handler)

    return app