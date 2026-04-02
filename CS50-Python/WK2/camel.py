user_input = input("camelCase :")
snake_case = ' '
for i in user_input:
    if (i.isupper()):
        snake_case = snake_case + "_" + i.lower()
    else:
        snake_case = snake_case + i

print(snake_case)



