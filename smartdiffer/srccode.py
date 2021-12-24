import os
from typing import Tuple, Optional
from pathlib import Path


from smartdiffer import etherscan_api


def retrieve_from(left_src: str, right_src: str) -> Optional[Tuple[str, str]]:
    left_src_code = _retrieve_sourcecode(left_src)
    right_src_code = _retrieve_sourcecode(right_src)
    if left_src_code and right_src_code:
        return left_src_code, right_src_code
    return None


def _retrieve_sourcecode(src: str) -> Optional[str]:
    src_code = __get_sourcecode_from_file(src)
    if src_code is not None:
        return src_code
    src_code = etherscan_api.get_sourcecode_from_contract(address=src)
    return src_code


def __get_sourcecode_from_file(rel_path: str) -> Optional[str]:
    cwd = Path(os.getcwd()).absolute()
    filepath = os.path.join(cwd, rel_path)
    try:
        with open(filepath, 'r') as f:
            src_code = f.read()
    except FileNotFoundError:
        return None
    return src_code
