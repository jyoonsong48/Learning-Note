import random


def main():
    while True:
        try:
            level = get_level()
            score = 10
            for i in range(10):
                x = generate_integer(level)
                y = generate_integer(level)
                answer = x+y
                for a in range(3):
                    user_a = input(f"{x} + {y} = ")
                    if user_a.isnumeric == False:
                        continue # 다시 인풋 받기
                    else:
                        user_answer = int(user_a)
                        if answer == user_answer:
                            break # 다음 문제로 넘어가기
                        if a == 2 and user_answer != answer:
                            print(f"{x} + {y} = {x+y}")
                            score = score - 1
                        if a != 2 and user_answer != answer:
                            print("EEE")
            print(f"Score: {score}")
            break
        except EOFError:
            break


def get_level():
    while True:
        try:
            user_l = input("Level:")
        except EOFError:
            break
        if user_l.isnumeric() == False:
            continue
        else:
            user_level = int(user_l)
            if user_level > 3:
                continue
            if user_level < 1:
                continue
            else:
                level = user_level
                return level
                break


def generate_integer(level):
    if level == 1:
        n =random.randint(0, 9)
        return n
    if level == 2:
        n =random.randint(10, 99)
        return n
    if level == 3:
        n =random.randint(100, 999)
        return n
    else:
        raise ValueError


if __name__ == "__main__":
    main()
