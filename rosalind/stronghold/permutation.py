from itertools import permutations

n = '' # number here
nlist = list(range(1, n+1))

permu = list(permutations(nlist, n))
total = str(len(permu))


with open("permutation.txt", "w") as f:
    f.write(total)
    for item in permu:
        line  = ' '.join(map(str, item))
        f.write(f"\n{line}")
