import sys
import re
import inflect
from datetime import date

p = inflect.engine()

def main():
    user_date = input("Date of Birth: ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", user_date):
        sys.exit("Invalid date")
    try:
        birth_date = date.fromisoformat(user_date)
    except ValueError:
        sys.exit("Invalid date")
    minutes = (date.today() - birth_date).days * 1440
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")

if __name__ == "__main__":
    main()
