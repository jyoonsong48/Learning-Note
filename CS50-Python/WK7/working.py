import re
# import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'[0-9]{1,2}+(?::[0-9]{1,2})?\s+(?:AM|PM)\s+to\s+[0-9]{1,2}(?::[0-9]{1,2})?\s+(?:AM|PM)' # "0-9" "(:0-9)" " " "AM or PM" "to" ...
    if not re.fullmatch(pattern, s):
        raise ValueError
    time_pattern = r'[0-9]+(?::[0-9]+)?\s*(?:AM|PM)'
    time = re.findall(time_pattern, s)
    times = []
    for t in time:
        t = t.replace(" ", "")
        if "AM" in t:
            t = t.replace("AM", "")
            parts = t.split(":")

            if int(parts[0]) == 12:
                hr = 0
            elif int(parts[0]) > 12:
                raise ValueError
            else:
                hr = int(parts[0])


            if not len(parts) > 1:
                min = 0
            else:
                if int(parts[1]) >= 60:
                    raise ValueError
                else:
                    min = int(parts[1])
            times.append((hr, min))

        if "PM" in t:
            t = t.replace("PM", "")
            parts = t.split(":")

            if int(parts[0]) == 12:
                hr = 12
            elif int(parts[0]) > 12:
                raise ValueError
            else:
                hr = int(parts[0]) + 12


            if not len(parts) > 1:
                min = 0
            else:
                if int(parts[1]) >= 60:
                    raise ValueError
                else:
                    min = int(parts[1])
            times.append((hr, min))

    start_hr, start_min = times[0]
    end_hr, end_min = times[-1]
    nton = f"{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}"
    return nton



if __name__ == "__main__":
    main()
