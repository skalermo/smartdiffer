import argparse
import sys


from smartdiffer import config
from smartdiffer import diffchecker
from smartdiffer import srccode


def main():
    parser = argparse.ArgumentParser(
        prog='smartdiff', 
        description='Tool to compare smart contracts source code', 
    )
    parser.add_argument(
        'left_source', help='Source on the left', type=str, metavar='LEFT'
    )
    parser.add_argument(
        'right_source', help='Source on the right', type=str, metavar='RIGHT'
    )
    args = parser.parse_args()

    if not args.left_source or not args.right_source:
        parser.print_help()
        return 1

    config.load_api_keys()
    if (res := srccode.retrieve_from(args.left_source, args.right_source)) is None:
        print('Cannot retrieve source.')
        raise Exception
    else:
        left, right = res

    diffchecker.prep_diff(left, right)
    return 0


if __name__ == "__main__":
    sys.exit(main())
