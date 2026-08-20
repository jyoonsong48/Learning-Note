import re
from collections import Counter

with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]

def complement(str):
    replace = str.maketrans('ACGT', 'TGCA')
    complement = str.translate(replace)
    complement = complement[::-1]
    return complement

def HammingDistance(p,q):
    dist = 0
    for i in range(len(p)): 
        if p[i] != q[i]: dist += 1 
        else: dist = dist + 0
    return dist

complement_seq = []
for i in range(len(sequences)):
    complements = complement(sequences[i])
    complement_seq.append(complements)

seq_counts = Counter(sequences)
sequences_set = set(sequences)
matched = set()

for i, seq in enumerate(sequences):
    comp = complement_seq[i]
    
    if comp in sequences_set:
        matched.add(seq)
        matched.add(comp)
    
    if seq_counts[seq] > 1:
        matched.add(seq)

errors = [seq for seq in sequences if seq not in matched]
# print(errors)
matched_seqs = list(dict.fromkeys([seq for seq in sequences + complement_seq if seq in matched or complement(seq) in matched]))
fixed = []
for error in errors:
    for sequence in matched_seqs:
        if HammingDistance(error, sequence) == 1:
            fixed.append(sequence)

with open("correction.txt", "w") as f:
    for error, sequence in zip(errors, fixed):
        f.write(f"{error}->{sequence}\n")


