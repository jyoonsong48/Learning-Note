from itertools import permutations, product

n = "number"

nlist = list(range(1, n+1))
signs = list(product([-1, 1], repeat=n))
permu = list(permutations(nlist, n))

total = []
for p in permu:
    for sign in signs:
        total.append(tuple(a * b for a, b in zip(p, sign)))

total_num = len(total)

with open("signed_permutation.txt", "w") as f:
    f.write(str(total_num))
    for item in total:
        line  = ' '.join(map(str, item))
        f.write(f"\n{line}")
