from itertools import product
import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]
sequence = sequences[0]

bases = ["A", "C", "G", "T"]
all_possible = [''.join(p) for p in product(bases, repeat=4)]
kmer_counts = {kmer: 0 for kmer in all_possible}

for i in range(len(sequence) - 3):
	pattern = sequence[i : i + 4]
	kmer_counts[pattern] += 1
	
result = [str(kmer_counts[kmer]) for kmer in all_possible]
result_write = " ".join(result)

with open("composition.txt", "w") as f:
    f.write(result_write)