n = "nth term of sequence"
m = "sliding window"


def fibonacci(n, m):
    F = [0] * (n+1)
    F[1] = 1
    F[2] = 0
    for i in range(3, n+1):
        F[i] = sum(F[max(0, i-m) : i-1])
        pair = sum(F[i-m+1: i+1])
    return pair

print(fibonacci(n, m))
