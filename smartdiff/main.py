import sys
import os
import json

import requests
from etherscan.contracts import Contract


WEB_URL = 'https://www.diffchecker.com/'
API_ENDPOINT = 'https://diffchecker-api-production.herokuapp.com'
ETHERSCAN_API_KEY = ''
AUTH_TOKEN = ''


def is_address(string: str):
    return string.startswith('0x')


def retrieve_code(source: str) -> str:
    code = ''
    if is_address(source):
        query_result = Contract(address=source, api_key=ETHERSCAN_API_KEY).get_sourcecode()
        source_code_json = json.loads(query_result[0]['SourceCode'][1:-1])
        sources_sorted = sorted(source_code_json['sources'].keys())
        code = '\n'.join(source_code_json['sources'][src]['content'] for src in sources_sorted)
    else:
        # if not address assume it is path to file with code
        path = os.path.realpath(source)
        with open(path, 'r') as f:
            code = f.read()
    return code


def make_post_req(left: str = '', right: str = ''):
    data = {
        'Authorization': 'Bearer ' + AUTH_TOKEN,
        'left': left,
        'right': right,
        'expiry': 'day',
        'title': '',
    }
    
    r = requests.post(url = API_ENDPOINT + '/diffs', json = data)
    return r


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f'Usage: python {sys.argv[0]} address/on/etherscan')
        exit(0)

    sources = sys.argv[1:]
    codes = ['' for _ in range(len(sources))]

    for i, source in enumerate(sources):
        code = retrieve_code(source)

        if not code:
            code = f'Cannot retrieve source code from source "{source}" !!!'

        codes[i] = code

    left, right = codes[0:2]

    response = make_post_req(left, right)
    url = WEB_URL + json.loads(response.text)['slug']
    print(f'Your diff is ready at {url}')


if __name__ == '__main__':
    with open('api_keys.json', mode='r') as key_file:
        keys = json.loads(key_file.read())
        ETHERSCAN_API_KEY = keys['etherscan']
        AUTH_TOKEN = keys['diffchecker']

    main()