TOKEN = (
    '*'
)
URL = 'https://yougile.com/api-v2/projects/'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}
HEADERS_NO_AUTH = {
    'Content-Type': 'application/json'
}
