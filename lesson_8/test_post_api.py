import requests


TOKEN = (
    '*'
)
URL = 'https://yougile.com/api-v2/projects'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}


def test_post_project():  # позитивный тест
    body = {
            "title": "Домашняя работа",
            "users": {
                "89b42202-91ce-41aa-9726-1d7083f4ef1b": "admin"
            }

    }
    response = requests.post(URL, headers=HEADERS, json=body)
    print(response)
    assert response.status_code == 201


def test_post_project_empty_title():  # негативный тест
    body = {
            "title": "",
            "users": {
                "89b42202-91ce-41aa-9726-1d7083f4ef1b": "admin"
            }

    }
    response = requests.post(URL, headers=HEADERS, json=body)
    assert response.status_code == 400
