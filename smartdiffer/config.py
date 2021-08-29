import json
import os


DIFFCHECKER_AUTH_TOKEN: str
ETHERSCAN_API_KEY: str


def load_api_keys():
    home = os.path.expanduser('~')
    dirs = ['.', '..', home]
    keys = None

    for dir in dirs:
        try:
            key_file = open(dir + '/api_keys.json', mode='r')
        except:
            pass
        else:
            with key_file:
                keys = json.loads(key_file.read())

        if keys is None:
            print('Cannot locate file "api_keys.json"')
            raise FileNotFoundError

        global DIFFCHECKER_AUTH_TOKEN
        global ETHERSCAN_API_KEY
        DIFFCHECKER_AUTH_TOKEN = keys['diffchecker']
        ETHERSCAN_API_KEY = keys['etherscan']