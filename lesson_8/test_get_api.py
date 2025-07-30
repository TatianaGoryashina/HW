import requests


TOKEN = (
    '*'
)
URL = (
    'https://yougile.com/api-v2/projects/'
)


def test_get_project_by_id():  # позитивный тест
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 200


def test_get_project_by_id_no_auth():  # негативный тест
    HEADERS = {
        'Content-Type': 'application/json'
    }
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 401
