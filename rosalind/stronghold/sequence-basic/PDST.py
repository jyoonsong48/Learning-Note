import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()


sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]
#print(sequences)
n = len(sequences)
matrix = [[0.0] * n for _ in range(n)]
for i in range(len(sequences)):
    for j in range(len(sequences)):
        dist = 0
        for p in range(len(sequences[i])): 
            if sequences[i][p] != sequences[j][p]:
                dist += 1 
            else: dist = dist + 0
        pdist = dist / (len(sequences[i]))
        matrix[i][j] = dist / len(sequences[i])

for row in matrix:
    print(" ".join(f"{x:.3f}" for x in row))
        
