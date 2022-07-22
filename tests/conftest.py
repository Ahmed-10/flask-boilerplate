import pytest
from api import create_app
from api.models import db

@pytest.fixture(scope="session")
def app():
    app = create_app('api.config.TestingConfig')

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()