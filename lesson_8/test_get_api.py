import requests
from config import URL
from config import HEADERS
from config import HEADERS_NO_AUTH


def test_get_project_by_id():  # позитивный тест
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 200


def test_get_project_by_id_no_auth():  # негативный тест
    response = requests.get(URL, headers=HEADERS_NO_AUTH)
    assert response.status_code == 401
