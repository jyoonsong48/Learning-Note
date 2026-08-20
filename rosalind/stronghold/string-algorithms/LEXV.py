from itertools import product

with open("rosalind_lexv.txt", 'r', encoding='utf-8') as f:
    dataset = f.read()

data = dataset.split("\n")
data.remove("")
n = int(data[-1])
del data[-1]
alphabets = [a.split() for a in data][0]
print(n, alphabets)
every = []
for i in range(1, n+1):
    every.extend(list(product(alphabets, repeat=i)))

every = sorted(every, key=lambda x: [alphabets.index(c) for c in x])

# print(*[''.join(t) for t in every])

with open("varied_length.txt", "w") as f:
    for item in every:
        f.write(f"{''.join(item)}\n")
