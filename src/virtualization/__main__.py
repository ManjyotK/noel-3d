import json
import sys


def main():
    print(sys.argv)
    with open(sys.argv[1], "r") as f:
        data = json.load(f)
    print(data)
