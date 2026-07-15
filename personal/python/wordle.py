from english_words import get_english_words_set
import random

words = list(get_english_words_set(['web2'], alpha=True, lower=True))
user_length = int(input("How many letters?:"))

def group_by_length(words):
    grouped_words = []
    for word in words:
        length = len(word)
        if length == user_length:
            grouped_words.append(word)
    return grouped_words


def guessing(word_list):
    answer = random.choice(word_list)
    count = 0
    while True:
        guess = input("\n Guess the word:")
        if len(guess) != len(answer):
            continue
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                print("\033[32m" + guess[i] + "\033[0m", end="")
            elif guess[i] != answer[i] and guess[i] in answer:
                print("\033[33m" + guess[i] + "\033[0m", end="")
            else:
                print("\033[31m" + guess[i] + "\033[0m", end="")
        if guess == answer:
            print("\nBingo!")
            if count == 0:
                print(f"It took you 1 try! How tf did you do that")
            if count < 5:
                print(f"It took you {count} tries! Good!")
            if 5 <= count <= 15:
                print(f"It took you {count} tries!")
            if count >= 16:
                print(f"It took you {count} tries! meh")
            break
        else:
            count += 1
            continue
            
def main():
    word_list = group_by_length(words)
    guessing(word_list)
    
if __name__ == '__main__':
    main()

