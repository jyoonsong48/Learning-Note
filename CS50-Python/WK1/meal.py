def main():
    time = input("What time is it?:")
    now = convert(time)
    if 7 <= now <= 8:
        print("breakfast time")
    elif 12 <= now <= 13:
        print("lunch time")
    elif 18 <= now <= 19:
        print("dinner time")

def convert(time):
    time = time.strip()
    hours, minutes = time.split(":")
    m = (int(minutes) / 60)
    h = int(hours)
    now = float(m+h)
    return now

if __name__ == "__main__":
    main()


