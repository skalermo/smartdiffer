import os
from typing import Tuple, Optional
from pathlib import Path


from smartdiffer import etherscan_api


def retrieve_from(left_src: str, right_src: str) -> Optional[Tuple[str, str]]:
    src_codes = (
        _retrieve_sourcecode(left_src),
        _retrieve_sourcecode(right_src),
    )
    if not all(src_codes):
        return None
    return src_codes


def _retrieve_sourcecode(src: str) -> Optional[str]:
    src_code = __get_sourcecode_from_file(src)
    if src_code is not None:
        return src_code
    return etherscan_api.get_sourcecode_from_contract(address=src)


def __get_sourcecode_from_file(rel_path: str) -> Optional[str]:
    try:
        cwd = Path(os.getcwd()).absolute()
        filepath = os.path.join(cwd, rel_path)
        f = open(filepath, 'r')
    except FileNotFoundError:
        return None
    else:
        with f:
            src_code = f.read()
    return src_code
