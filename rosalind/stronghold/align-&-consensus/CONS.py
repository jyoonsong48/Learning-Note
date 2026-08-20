import re
with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

#dataset = or enter manually
sequences = dataset.split(">")
sequences = [s.replace('\n', '') for s in sequences]
ID = [item for s in sequences for item in re.findall(r'Rosalind_\d\d\d\d', s) if item]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d\d\d\d', s) if item]

letter = []
sequence_for_length = len(sequences[0])
for i in range(sequence_for_length):
    ith_letter = [sequence[i] for sequence in sequences]
    letter.append(ith_letter)

counts_A = []
counts_C = []
counts_G = []
counts_T = []

for i in range(len(letter)):
    count_A = letter[i].count("A")
    count_C = letter[i].count("C")
    count_G = letter[i].count("G")
    count_T = letter[i].count("T")
    counts_A.append(count_A)
    counts_C.append(count_C)
    counts_G.append(count_G)
    counts_T.append(count_T)

consensus = []
for i in range(sequence_for_length):
    max_count = max(counts_A[i], counts_C[i], counts_G[i], counts_T[i])
    if counts_A[i] == max_count:
        consensus.append("A")
    elif counts_C[i] == max_count:
        consensus.append("C")
    elif counts_G[i] == max_count:
        consensus.append("G")
    else:
        consensus.append("T")

result = "".join(consensus) + "\n"
result += "A: " + " ".join(map(str, counts_A)) + "\n"
result += "C: " + " ".join(map(str, counts_C)) + "\n"
result += "G: " + " ".join(map(str, counts_G)) + "\n"
result += "T: " + " ".join(map(str, counts_T)) + "\n"

print(result)

with open("output.txt", "w") as f:
    f.write(result)