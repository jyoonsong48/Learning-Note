import re
with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

sequences = dataset.split(">")
sequences = [s.replace('\n', '') for s in sequences]
ID = [item for s in sequences for item in re.findall(r'Rosalind_\d\d\d\d', s) if item]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d\d\d\d', s) if item]

prefix = []
suffix = []

for DNA in sequences:
    pre = DNA[:3]
    suf = DNA[-3:]
    prefix.append(pre)
    suffix.append(suf)

for i in range(len(prefix)):
    for j in range(len(suffix)):
        if i != j and suffix[i] == prefix[j]:
            print(ID[i], ID[j])