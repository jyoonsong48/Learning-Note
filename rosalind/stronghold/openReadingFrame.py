codon_table_DNA = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',    # Serine
    'TTC': 'F', 'TTT': 'F',    # Phenylalanine
    'TTA': 'L', 'TTG': 'L',    # Leucine
    'TAC': 'Y', 'TAT': 'Y',    # Tirosine
    'TAA': '*', 'TAG': '*',    # Stop
    'TGC': 'C', 'TGT': 'C',    # Cisteine
    'TGA': '*',    # Stop
    'TGG': 'W',    # Tryptofan
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',    # Leucine
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',    # Proline
    'CAC': 'H', 'CAT': 'H',    # Histidine
    'CAA': 'Q', 'CAG': 'Q',    # Glutamine
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',    # Arginine
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I',    # Isoleucine
    'ATG': 'M',    # Methionine
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',    # Threonine
    'AAC': 'N', 'AAT': 'N',    # Asparagine
    'AAA': 'K', 'AAG': 'K',    # Lysine
    'AGC': 'S', 'AGT': 'S',    # Serine
    'AGA': 'R', 'AGG': 'R',    # Arginine
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',    # Valine
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',    # Alanine
    'GAC': 'D', 'GAT': 'D',    # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',    # Glutamic Acid
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'     # Glycine
}
import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

str = dataset.split("\n")
sequences = [item for s in str for item in re.split(r'>Rosalind_\d\d\d\d', s) if item]

sequence = "".join(sequences)
replace = sequence.maketrans('ACGT', 'TGCA')
complement_seq = sequence.translate(replace)
complement_seq = complement_seq[::-1]


def open_reading_frame(sequence):
    results = []
    for i in range(len(sequence)):
        window = sequence[i:i+3]
        if window == "ATG":
            protein = []
            for j in range(i, len(sequence), 3):
                codon = sequence[j:j+3]
                if codon in ("TGA", "TAA", "TAG"):
                    results.append("".join(protein))
                    break
                protein.append(codon_table_DNA.get(codon, ""))
    return results

result = sorted(set(open_reading_frame(sequence) + open_reading_frame(complement_seq)))
for r in result:
    print(r)

     