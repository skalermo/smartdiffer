import sys
import json

import requests
from etherscan.contracts import Contract


WEB_URL = 'https://www.diffchecker.com/'
API_ENDPOINT = 'https://diffchecker-api-production.herokuapp.com'
AUTH_TOKEN = ''


def is_address(string: str):
    return string.startswith('0x')


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

    addresses = sys.argv[1:]
    sources = ['' for _ in range(len(addresses))]

    with open('api_keys.json', mode='r') as key_file:
        keys = json.loads(key_file.read())
        key = keys['etherscan']
        AUTH_TOKEN = keys['diffchecker']

    for i, address in enumerate(addresses):
        contract = Contract(address=address, api_key=key)
        sourcecode = contract.get_sourcecode()

        if not sourcecode:
            print('No source code found')
            return

        query_result = json.loads(sourcecode[0]['SourceCode'][1:-1])
        sources_sorted = sorted(query_result['sources'].keys())

        sources[i] = '\n'.join(query_result['sources'][src]['content'] for src in sources_sorted)
        # with open(address, 'w') as f:
        #     f.write(source)

    left, right = sources[0:2]

    response = make_post_req(left, right)
    url = WEB_URL + json.loads(response.text)['slug']
    print(f'Your diff is ready at {url}')

if __name__ == '__main__':
    main()