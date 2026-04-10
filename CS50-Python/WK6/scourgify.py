import pandas as pd
import sys

if len(sys.argv) < 3:
    print("Too few commend-line arguments")
    sys.exit(1)
if len(sys.argv) > 3:
    print("Too many commend-line arguments")
    sys.exit(1)

while True:
    try:
        before = pd.read_csv(f"{sys.argv[1]}")
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        before[['last', 'first']] = before['name'].str.split(', ', expand=True)
        before = before.drop(columns=['name'])
        new_order = ['first', 'last', 'house']
        before = before[new_order]
        before.to_csv(f"{sys.argv[2]}", index=False)
        break
