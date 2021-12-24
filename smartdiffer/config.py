import json
import os


DIFFCHECKER_AUTH_TOKEN: str = ''
ETHERSCAN_API_KEY: str = ''


def load_api_keys() -> None:
    home = os.path.expanduser('~')
    dirs = [home, '.', '..']
    keys = None

    for dir in dirs:
        try:
            with open(dir + '/api_keys.json', mode='r') as key_file:
                keys = json.loads(key_file.read())
        except FileNotFoundError:
            pass
        else:
            break

    if keys is None:
        print('Cannot locate file "api_keys.json"')
        raise FileNotFoundError

    global DIFFCHECKER_AUTH_TOKEN
    global ETHERSCAN_API_KEY
    DIFFCHECKER_AUTH_TOKEN = keys['diffchecker']
    ETHERSCAN_API_KEY = keys['etherscan']


def get_diffchecker_auth_token() -> str:
    return DIFFCHECKER_AUTH_TOKEN


def get_etherscan_api_key() -> str:
    return ETHERSCAN_API_KEY
