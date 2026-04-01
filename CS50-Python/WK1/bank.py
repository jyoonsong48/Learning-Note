greetings = input("Greeting :")
def bank(greetings):
    H = greetings.lower().strip().startswith("hello")
    Y = (greetings[0]).lower().strip()
    if H:
        print("$0")
    elif Y == "h":
        print("$20")
    else:
        print("$100")

bank(greetings)
