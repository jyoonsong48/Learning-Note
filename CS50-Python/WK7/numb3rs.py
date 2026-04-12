# import re
# import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if str(int(part)) != part:
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True


if __name__ == "__main__":
    main()
