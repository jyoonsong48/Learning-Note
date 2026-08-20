from math import factorial

RNA = "insert RNA sequence here"

a = int(RNA.count("A"))
c = int(RNA.count("C"))
g = int(RNA.count("G"))
u = int(RNA.count("U"))

assert a == u, f"A({a}) != U({u})"
assert c == g, f"C({c}) != G({g})"

result = factorial(a) * factorial(c)
print(result)