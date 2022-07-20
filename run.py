import os
from api import create_app


if os.environ.get("FLASK_ENV") == "development":
    app = create_app('api.config.DevelopmentConfig')
else:
    app = create_app('api.config.ProductionConfig')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
