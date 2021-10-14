import json
from typing import Optional


from etherscan.contracts import Contract


from smartdiffer.config import get_etherscan_api_key


def get_sourcecode_from_contract(address: str) -> Optional[str]:
    if not _is_valid_address(address):
        return None
    try:
        query_result = Contract(address=address, api_key=get_etherscan_api_key()).get_sourcecode()
    except:
        return None
    return _get_sourcecode_from(query_result)


def _is_valid_address(string: str) -> bool:
    return string.startswith('0x') and len(string) == 2 + 20 * 2 and _is_hex(string[2:])


def _is_hex(string: str) -> bool:
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def _get_sourcecode_from(query_result) -> str:
    source_code_json = json.loads(query_result[0]['SourceCode'][1:-1])
    sources = source_code_json['sources'].keys()
    code = '\n'.join(source_code_json['sources'][src]['content'] for src in sources)
    return code

