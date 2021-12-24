import json
from typing import Optional


from etherscan.contracts import Contract


from smartdiffer.config import get_etherscan_api_key


def get_sourcecode_from_contract(address: str) -> Optional[str]:
    if not _is_valid_address(address):
        return None
    try:
        query_result = Contract(
            address=address, api_key=get_etherscan_api_key()
        ).get_sourcecode()
    except ConnectionRefusedError:
        return None
    return _get_sourcecode_from(query_result)


def _is_valid_address(addr: str) -> bool:
    expected_length = 2 + 20 * 2
    return addr.startswith('0x') and \
        len(addr) == expected_length and _is_hex(addr[2:])


def _is_hex(string: str) -> bool:
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def _get_sourcecode_from(query_result) -> str:  # type: ignore[no-untyped-def]
    src_json = json.loads(query_result[0]['SourceCode'][1:-1])
    sources = src_json['sources'].keys()
    return '\n'.join(src_json['sources'][s]['content'] for s in sources)
