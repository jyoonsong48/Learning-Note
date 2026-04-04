from collections import Counter
grocery_list = []
while True:
    try:
        item = input()
        grocery_list.append(item)
    except EOFError:
        upper_grocery_list = [word.upper() for word in grocery_list]
        sorted_grocery_list =sorted(upper_grocery_list)
        grocery = dict(Counter(sorted_grocery_list))
        for key, value in grocery.items():
            print(f"{value} {key}")
        break
    else:
        continue

