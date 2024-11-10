import sys
from ._schema import Animation


def main():
    print(sys.argv)

    with open(sys.argv[1]) as f:
        data = f.read()
    animation = Animation.model_validate_json(data)

    print(animation)
