from Bio import Phylo
from io import StringIO

def get_distance_with_biopython(newick_str, name1, name2):
    tree = Phylo.read(StringIO(newick_str), "newick")
    for clade in tree.find_clades():
        clade.branch_length = 1
    return tree.distance(name1, name2)

dataset = """insert newick string
and two nodes here"""

dataset = dataset.split("\n")
data = []
temp = []
for item in dataset:
    if item == "":
        data.append(temp)
        temp = []
    else:
        temp.append(item)
data.append(temp)

answer = []
for d in data:
    x, y = d[1].split(" ")
    answer.append(get_distance_with_biopython(d[0], x, y))

print(*answer)