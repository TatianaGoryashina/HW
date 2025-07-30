import requests


BEARER_TOKEN = (
    '*'
)
URL = (
    'https://yougile.com/api-v2/projects/'
)

HEADERS = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json'
}


def test_put_project_by_id():  # позитивный тест
    body = {
        "deleted": True,
        "title": "Домашняя работа",
        "users": {
            "89b42202-91ce-41aa-9726-1d7083f4ef1b": "admin"
        }
    }
    response = requests.put(URL + '0dfddb0c-bcc1-4243-9e49-fe9f8c012d9c',
                            headers=HEADERS, json=body)
    assert response.status_code == 200


def test_put_project_by_no_id():  # негативный тест
    response = requests.put(URL, headers=HEADERS)
    assert response.status_code == 404
