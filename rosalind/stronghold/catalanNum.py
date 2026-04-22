import re
from functools import lru_cache

dataset = """insert sequence here"""
str = dataset.split("\n")
sequence = [item for s in str for item in re.split(r'>Rosalind_\d+', s) if item]
sequence = sequence[0]

def is_match(a, b):
    return (a, b) in [("A", "U"), ("U", "A"), ("G", "C"), ("C", "G")]

@lru_cache(maxsize=None)
def count_matching(s):
    if len(s) == 0:
        return 1  
    
    total = 0
    for j in range(1, len(s), 2): 
        if is_match(s[0], s[j]):
            inner = s[1:j]
            outer = s[j+1:] 
            total += count_matching(inner) * count_matching(outer)
    
    return total % 1_000_000

print(count_matching(sequence))