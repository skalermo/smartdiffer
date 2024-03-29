import requests
import json


from smartdiffer.config import get_diffchecker_auth_token


API_ENDPOINT = 'https://api.diffchecker.com'
WEB_URL = 'https://www.diffchecker.com/'


def prep_diff(left: str, right: str) -> str:
    response = _send_post_request(left, right)
    url = _retrieve_url(response)
    print(f'Your diff is ready at {url}')
    return url


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
