from fractions import Fraction
while True:
    try:
        fr = input("Fraction: ")
        f = Fraction(fr)
    except ZeroDivisionError:
        continue
    except ValueError:
        continue
    if f > 1 or f < 0:
        continue
    else:
        if 1 >= f >= 0.99:
            print("F")
            break
        if 0 <= f <= 0.01:
            print("E")
            break
        else:
            print(f"{round(f * 100)}%")
            break
