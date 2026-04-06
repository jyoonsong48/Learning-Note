import random


while True:
    try:
        user_l = input("Level:")
    except EOFError:
        break
    if user_l.isnumeric() == False:
        continue
    else:
        user_level = int(user_l)
        if user_level < 0:
            continue
        else:
            answer = random.randint(1, user_level)
            while True:
                try:
                    user_g = input("Guess?:")
                    if user_g.isnumeric() == False:
                        continue
                    else:
                        user_guess = int(user_g)
                        if user_guess > answer:
                            print("Too large!")
                            continue
                        elif 0 < user_guess < answer:
                            print("Too small!")
                            continue
                        elif user_guess <= 0:
                            continue
                        else:
                            break
                except EOFError:
                    break
        if answer == user_guess:
            print("Just right!")
            break

