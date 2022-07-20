from flask import Flask, render_template


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    def index():
        return 'Hello, World!'
    app.add_url_rule('/', 'index', index)
    return app