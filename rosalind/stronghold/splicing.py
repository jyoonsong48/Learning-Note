import re
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
with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()


dataset = data.split(">")
sequences = [item for s in dataset for item in re.split(r'Rosalind_\d+\n', s) if item]
sequences = [item.replace("\n", "") for item in sequences]


RNA = sequences[0]
intron = []


for i in range(len(sequences)):
    if i != 0:
        intron.append(sequences[i])

def splicing(RNA, intron):
    spliced_RNA = RNA
    for i in range(len(intron)):
        if intron[i] in RNA:
            spliced_RNA = spliced_RNA.replace(intron[i], "")
    return spliced_RNA

def translate(str):
    codon = [str[i:i+3] for i in range(0, len(str), 3)]
    aa = [codon_table_DNA.get(item, item) for item in codon]
    aa = ''.join(aa)
    aa = aa.replace("*", "")
    return aa

result = translate(splicing(RNA, intron))

with open("RNA_splicing.txt", "w") as f:
    f.write(result)