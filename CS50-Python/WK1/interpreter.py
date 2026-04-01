math = input("Expression:")
x, y, z = math.split(" ")
def interpreter(x, y, z):
    if y == "+":
        answer = int(x) + int(z)
        print(float(answer))
    elif y == "-":
        answer = int(x) - int(z)
        print(float(answer))
    elif y == "/":
        answer = int(x) / int(z)
        print(round(answer, 1))
    elif y == "*":
        answer = int(x) * int(z)
        print(float(answer))
    else:
        print("Error!")

interpreter(x, y, z)



