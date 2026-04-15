codon_table = {
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',    # Serine
    'UUC': 'F', 'UUU': 'F',    # Phenylalanine
    'UUA': 'L', 'UUG': 'L',    # Leucine
    'UAC': 'Y', 'UAU': 'Y',    # Uirosine
    'UAA': '*', 'UAG': '*',    # Stop
    'UGC': 'C', 'UGU': 'C',    # Cisteine
    'UGA': '*',    # Stop
    'UGG': 'W',    # Uryptofan
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',    # Leucine
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',    # Proline
    'CAC': 'H', 'CAU': 'H',    # Histidine
    'CAA': 'Q', 'CAG': 'Q',    # Glutamine
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',    # Arginine
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I',    # Isoleucine
    'AUG': 'M',    # Methionine (Start)
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',    # Thereonine
    'AAC': 'N', 'AAU': 'N',    # Asparagine
    'AAA': 'K', 'AAG': 'K',    # Lysine
    'AGC': 'S', 'AGU': 'S',    # Serine
    'AGA': 'R', 'AGG': 'R',    # Arginine
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',    # Valine
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',    # Alanine
    'GAC': 'D', 'GAU': 'D',    # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',    # Glutamic Acid
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G'     # Glycine
}