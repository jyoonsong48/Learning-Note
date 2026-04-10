import sys
import pandas as pd
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few commend-line arguments")
    sys.exit(1)
if len(sys.argv) > 2:
    print("Too many commend-line arguments")
    sys.exit(1)
if sys.argv[1].endswith(".csv") == False:
        print("Not a CSV file")
        sys.exit(1)
while True:
    try:
        menu = pd.read_csv(f"{sys.argv[1]}")
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        headers = [f"{sys.argv[1][:-4].capitalize()} Pizza", "Small", "Large"]
        print(tabulate(menu, headers = headers, tablefmt="grid", showindex=False))
        break
