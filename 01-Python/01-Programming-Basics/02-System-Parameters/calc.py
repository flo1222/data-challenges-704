# pylint: disable=missing-module-docstring,missing-function-docstring

import sys

def main():
    """A calculator limited to 2 arguments"""
    if str(sys.argv[2]) == '+':
        return int(sys.argv[1]) + int(sys.argv[3])
    if str(sys.argv[2]) == '-':
        return int(sys.argv[1]) - int(sys.argv[3])
    # else: #str(sys.argv[2]) == '*':
    return int(sys.argv[1]) * int(sys.argv[3])
    # return None

if __name__ == "__main__":
    print(main())
