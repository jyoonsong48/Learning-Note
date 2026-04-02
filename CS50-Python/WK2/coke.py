print(f"Amount Due: 50")
coin = 0
amount_due = 50
while amount_due > 0:

    coin = int(input("Insert Coin:"))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin
        print(f"Amount Due: {amount_due}")
    else:
        amount_due = amount_due
        print(f"Amount Due: {amount_due}")

else:
    change_owed_print = abs(amount_due)
    print(f"Change Owed: {change_owed_print}")

