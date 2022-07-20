from api import create_app


def test_config():
    assert not create_app('api.config.ProductionConfig').testing
    assert create_app('api.config.TestingConfig').testing


def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'