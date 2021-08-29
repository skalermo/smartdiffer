import requests
import json


API_ENDPOINT = 'https://diffchecker-api-production.herokuapp.com'
WEB_URL = 'https://www.diffchecker.com/'


def prep_diff(left: str, right: str) -> str:
    response = _send_post_request(left, right)
    url = _retrieve_url(response)
    print(f'Your diff is ready at {url}')
    return url


def _send_post_request(left: str = '', right: str = ''):
    from smartdiffer.config import DIFFCHECKER_AUTH_TOKEN

    data = {
        'Authorization': 'Bearer ' + DIFFCHECKER_AUTH_TOKEN,
        'left': left,
        'right': right,
        'expiry': 'day',
        'title': '',
    }
    return requests.post(url = API_ENDPOINT + '/diffs', json = data)


def _retrieve_url(response):
    return WEB_URL + json.loads(response.text)['slug']