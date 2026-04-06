import inflect
p = inflect.engine()

name = []

while True:
    try:
        user_input = input("Name:")
        name.append(user_input)
    except EOFError:
        print()
        if len(name) == 1:
            print(f"Adieu, adieu, to {name[0]}")
            break
        for i in range(len(name)):
            if i == 0:
                print(f"Adieu, adieu, to {name[0]}")
            else:
                names = name[0:i+1]
                say_bye = p.join(names)
                print(f"Adieu, adieu, to {say_bye}")
        break
