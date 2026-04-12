import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    match = re.findall(r"\bum\b", s)
    um_count = len(match)
    return um_count


if __name__ == "__main__":
    main()
