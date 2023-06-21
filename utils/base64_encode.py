import argparse
import base64


def encode_base64(string: str) -> str:
    bytes = string.encode("UTF-8")
    return base64.b64encode(bytes).decode("ascii")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", type=str, help="string for encoding to base64")

    args = parser.parse_args()
    print(encode_base64(args.string))



