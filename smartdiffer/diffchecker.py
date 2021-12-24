import requests
import json


from smartdiffer.config import get_diffchecker_auth_token


API_ENDPOINT = 'https://diffchecker-api-production.herokuapp.com'
WEB_URL = 'https://www.diffchecker.com/'


def get_diff_url(left: str, right: str) -> str:
    response = _send_post_request(left, right)
    return _retrieve_url(response)


def _send_post_request(left: str = '', right: str = '') -> requests.Response:
    data = {
        'Authorization': 'Bearer ' + get_diffchecker_auth_token(),
        'left': left,
        'right': right,
        'expiry': 'day',
        'title': '',
    }
    return requests.post(url=API_ENDPOINT + '/diffs', json=data)


def _retrieve_url(response: requests.Response) -> str:
    return WEB_URL + str(json.loads(response.text)['slug'])
