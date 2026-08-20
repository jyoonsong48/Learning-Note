from math import comb

n = "number"
m = "number"

total = 0
for i in range(m, n+1):
    answer = comb(n, i)
    total = total + answer


print(total % 1000000)
    