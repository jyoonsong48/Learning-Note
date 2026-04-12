import re
# import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        vid_id = match.group(2)
        link = f"https://youtu.be/{vid_id}"
        return link

    return None


if __name__ == "__main__":
    main()
