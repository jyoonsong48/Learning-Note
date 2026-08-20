import re

with open("insert file path here", 'r', encoding='utf-8') as f:
   data = f.read()


str = data.split(">")
seq_n_pattern = [item for s in str for item in re.split(r'Rosalind_\d\d+', s) if item]
seq_n_pattern = [s.replace('\n', '') for s in seq_n_pattern if s.strip()]

sequence = seq_n_pattern[0]
pattern = seq_n_pattern[1]
positions = []

j = 0
for i in range(len(sequence)):
        if sequence[i] == pattern[j]:
            positions.append(i+1)
            j = j + 1
            if j == len(pattern):
                break

print(*positions)