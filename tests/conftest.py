import pytest
from api import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app('api.config.TestingConfig')

    yield app

@pytest.fixture
def client(app):
    return app.test_client()