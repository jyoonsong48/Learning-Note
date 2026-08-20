from math import factorial

n = "number"
k = "number"

partial_permutation = factorial(n) // factorial(n-k) % 1000000

print(partial_permutation)
