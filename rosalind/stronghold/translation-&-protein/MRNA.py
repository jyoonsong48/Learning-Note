CODON_COUNTS = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4,
    'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
    'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
}

#with open("rosalind_mprt.txt", 'r', encoding='utf-8') as f:
#    dataset = f.read()
dataset = "insert protein sequence here"

def infer(dataset):
    total_combo = 1
    modulo = 1000000
    for aa in dataset:
        total_combo = total_combo * CODON_COUNTS[aa]
        total_combo = total_combo % modulo
    
    total_combo = total_combo * 3
    total_combo = total_combo % modulo

    return total_combo

print(infer(dataset))


