import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]
sequence = sequences[0]
n = len(sequence)
P = [0] * n

k = 0
for i in range(1, n):
    while k > 0 and sequence[k] != sequence[i]:
        k = P[k - 1]
    if sequence[k] == sequence[i]:
        k += 1
    P[i] = k

print(*P)
with open("sped_up_finding.txt", "w") as f:
    for num in P:
        f.write(f"{str(num)} ")

