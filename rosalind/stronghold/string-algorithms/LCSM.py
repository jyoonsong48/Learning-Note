import re
with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()


sequences = dataset.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]

def shared_motif(sequences):
    min_length = len(min(sequences, key=len))
    shortest = min(sequences, key=len)
    for i in range(min_length, 0, -1):
        for j in range(len(shortest) - i + 1):
            kmer = shortest[j :j + i]
            if all(kmer in item for item in sequences):
                print(kmer)
                return kmer
            

shared_motif(sequences)
