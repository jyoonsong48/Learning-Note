from math import factorial, comb
import re

data = """sequence in FASTA format"""
sequences = data.split(">")
sequences = [s.replace('\n', '') for s in sequences]
sequences = [item for s in sequences for item in re.split(r'Rosalind_\d+', s) if item]
RNA = sequences[0]

a = int(RNA.count("A"))
c = int(RNA.count("C"))
g = int(RNA.count("G"))
u = int(RNA.count("U"))

k_au = min(a, u)
k_gc = min(g, c)

AU_ways = comb(a, k_au) * comb(u, k_au) * factorial(k_au)
GC_ways = comb(g, k_gc) * comb(c, k_gc) * factorial(k_gc)

print(AU_ways * GC_ways)