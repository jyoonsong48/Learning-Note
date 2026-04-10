import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few commend-line arguments")
    sys.exit(1)
if len(sys.argv) > 3:
    print("Too many commend-line arguments")
    sys.exit(1)
if sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith(".png") == False and sys.argv[1].endswith(".jpeg") == False:
    print("Invalid input")
    sys.exit(1)
if sys.argv[2].endswith(".jpg") == False and sys.argv[2].endswith(".png") == False and sys.argv[2].endswith(".jpeg") == False:
    print("Invalid output")
    sys.exit(1)
if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    print("Input and output have different extensions")
    sys.exit(1)

while True:
    try:
        shirt = Image.open("shirt.png")
        dressup = Image.open(f"{sys.argv[1]}")
        dressup = ImageOps.fit(dressup, shirt.size)
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
    else:
        dressup.paste(shirt, mask = shirt)
        dressup.save(f"{sys.argv[2]}")
        break
