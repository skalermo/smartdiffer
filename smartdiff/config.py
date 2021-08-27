import json


DIFFCHECKER_AUTH_TOKEN: str
ETHERSCAN_API_KEY: str


def load_api_keys():
    with open('../api_keys.json', mode='r') as key_file:
        keys = json.loads(key_file.read())

        global DIFFCHECKER_AUTH_TOKEN
        global ETHERSCAN_API_KEY
        DIFFCHECKER_AUTH_TOKEN = keys['diffchecker']
        ETHERSCAN_API_KEY = keys['etherscan']