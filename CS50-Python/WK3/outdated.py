import re
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        user_input = input("Date:")
        user_date = user_date = re.split(r'[\s/]', user_input)
    except EOFError:
        break
    if "/" not in user_input and user_date[0] not in month:
        continue
    else:
        if "/" in user_input:
            user_date = user_input.split('/')
            if user_date[0] in month:
                continue
            user_date = list(map(int, user_date))
            if user_date[0] > 12:
                continue
            if user_date[1] > 31:
                continue
            else:
                print(f"{user_date[2]}-{user_date[0]:02}-{user_date[1]:02}")
                break
        elif user_date[0] in month:
            user_date[0] = (month.index(user_date[0]) + 1)
            user_date = [str(i) for i in user_date]
            if user_date[1].endswith(",") == False:
                continue
            user_date = [item.replace(",", "") for item in user_date]
            user_date = list(map(int, user_date))
            if user_date[1] > 31:
                continue
            if user_date[0] > 12:
                continue
            else:
                print(f"{user_date[2]}-{user_date[0]:02}-{user_date[1]:02}")
                break
