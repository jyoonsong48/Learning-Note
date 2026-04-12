import validators

user_email = input("e-mail:")
if validators.email(user_email):
    print("Valid")
else:
    print("Invalid")
