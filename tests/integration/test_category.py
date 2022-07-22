import pytest

def test_get_all_categories(client):
    """
    Test get all categories
    """
    response = client.get('/api/categories/')
    assert response.status_code == 200

def test_add_category(client):
    """
    Test add category
    """
    response = client.post('/api/categories/', json={
        'name': 'Test Category'
    })
    assert response.status_code == 201
    assert response.json['data']['name'] == 'Test Category'

@pytest.fixture(scope="session")
def categories(client):
    """
    Create categories for tests
    """
    result = []
    for i in range(3):
        response = client.post('/api/categories/', json={
            'name': f"Test Category{i}"
        })
        result.append(response.json['data'])
    return result


def test_get_category(client, categories):
    """
    Test get category
    """
    response = client.get(f"/api/categories/{categories[0]['id']}")
    assert response.status_code == 200
    assert response.json['data']['name'] == f"Test Category{0}"

def test_update_category(client, categories):
    """
    Test update category
    """
    response = client.put(f"/api/categories/{categories[1]['id']}", json={
        'name': 'Test Category Updated'
    })
    assert response.status_code == 200
    assert response.json['data']['name'] == 'Test Category Updated'

def test_delete_category(client, categories):
    """
    Test delete category
    """
    response = client.delete(f"/api/categories/{categories[2]['id']}")
    assert response.status_code == 204
    assert response.data == b''