import re

dataset = """
insert dataset here
"""

sequences = dataset.split(">")
sequences = [s.replace('\n', '') for s in sequences]
ID = [item for s in sequences for item in re.findall(r'Rosalind_\d\d\d\d', s) if item]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d\d\d\d', s) if item]

GC =[]
index_GC = []
for index, DNA in enumerate(sequences):
    GC_content = (DNA.count("C") + DNA.count("G")) / len(DNA) * 100
    GC.append(GC_content)
    index_GC.append(index)
    GCdict = dict(zip(index_GC, GC))

max_GC = max(GCdict, key=GCdict.get)
n = max_GC

print(ID[n])
print(GCdict[max_GC])