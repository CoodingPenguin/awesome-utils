import argparse
import base64


def decode_base64(encoded_string: str) -> str:
    bytes = encoded_string.encode("ascii")
    return base64.b64decode(bytes).decode("UTF-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", type=str, help="encoded string for decoding")

    args = parser.parse_args()
    print(decode_base64(args.string))
