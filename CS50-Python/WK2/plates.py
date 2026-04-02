def plates():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if string[:2].isalpha() == False:
        return False
    if not 2 <= len(string) <= 6:
        return False
    if string.isalnum() == False:
        return False
    for i, char in enumerate(string):
        if char.isdigit():
            if char == "0":
                return False
            if string[i:].isdigit() == False:
                return False
            return True
    else:
        return True

plates()
