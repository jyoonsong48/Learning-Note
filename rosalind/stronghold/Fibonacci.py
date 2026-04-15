n = "n번째 항"
k = "더할 값 (cf. og 피보나치 수열: k = 1)"

def fibonacci(n, k):
    a, b, c = 1, 1, 1 + k
    for _ in range(n):
        print(a)
        a, b, c = b, c, c + (b * k) 

fibonacci(n, k)
    
# F(n)= F(n-1) + k * F(n-2)