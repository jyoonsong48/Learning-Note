from itertools import product
with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

dataset = data.split("\n")
n = int(dataset[-1])
del dataset[-1]
nlist = [char for item in dataset for char in item.split(" ")]

nPr = sorted(list(product(nlist, repeat = n)))

with open("lexi.txt", "w") as f:
    for item in nPr:
        line  = ''.join(map(str, item))
        f.write(f"{line}\n")
