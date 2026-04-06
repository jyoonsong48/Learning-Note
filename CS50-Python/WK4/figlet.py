from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)

if len(sys.argv) == 2:
    print("Invalid usage")
    sys.exit(1)
if len(sys.argv) == 3:
    if sys.argv[2] not in fonts:
        print("Invalid usage")
        sys.exit(1)
    if sys.argv[1] != "-f":
        print("Invalid usage")
        sys.exit(1)
    else:
        f = Figlet(font = sys.argv[2])

while True:
    try:
        user_input = input("Input: ")
    except EOFError:
        break
    if len(sys.argv) == 1:
        fig = Figlet(font=random_font)
        print(fig.renderText(user_input))
        sys.exit(0)
    else:
        output = f.renderText(user_input)
        print(output)
        break

