import re

dataset = """seqeunce here"""
data = dataset.split("\n")
del data[0]
sequence = data[0]
# print(sequence)

def is_match(a, b):
    return (a, b) in [("A", "U"), ("U", "A"), ("G", "C"), ("C", "G")]

def motzkin(str, n):
    dp = [[0] * n for _ in range(n)]

    for p in range(n):
        dp[p][p] = 1
        if p > 0:
            dp[p][p-1] = 1
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length - 1
            dp[i][j] = dp[i+1][j]
            for k in range(i+1, j+1):
                if is_match(str[i], str[k]):
                    left = dp[i+1][k-1] if k > i+1 else 1
                    right = dp[k+1][j] if k < j else 1
                    dp[i][j] += left * right
    return dp[0][n-1]

print(motzkin(sequence, len(sequence)) % 1000000)

