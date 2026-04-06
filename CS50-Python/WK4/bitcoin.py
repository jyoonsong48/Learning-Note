import sys
import requests
bitcoin = {"timestamp":1775474489690,"data":{"id":"bitcoin","rank":"1","symbol":"BTC","name":"Bitcoin","supply":"20012087.000000000000000000","maxSupply":"21000000.000000000000000000","marketCapUsd":"1394938121675.859863281250000000","volumeUsd24Hr":"30717175906.604835510253906250","priceUsd":"69704.779999999998835847","changePercent24Hr":"3.934756709445493","vwap24Hr":"68412.29711944099","explorer":"https://blockchain.info/","tokens":{}}}

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
if is_float(sys.argv[1]) == False:
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    n = float(sys.argv[1])
    p = 69704.779999999998835847
    pr = float(p) * n
    price = f"{pr:,.4f}"
    print(f"${price}")

# 06 April, 2026
