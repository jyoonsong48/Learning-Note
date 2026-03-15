### $\color{#fffff}{\text{2.2: Brute Force Algorithm for Motif Finding}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.2
# By: Jiyoon Song
# Content: Generating brute force algorithm for motif finding
# ==========================================================

DNA = [""] # insert DNA seqeunces here
k = 5 # insert the length of desired pattern here
d = 2 # insert maximum permissible error value here

def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighborhood = set()
    suffix_neighbors = Neighbors(Pattern[1:], d)
    for neighbor in suffix_neighbors:
        if HammingDistance(Pattern[1:], neighbor) < d:
            for base in ['A', 'C', 'G', 'T']:
                neighborhood.add(base + neighbor)
        else:
            neighborhood.add(Pattern[0] + neighbor)
    return neighborhood

def IsPatternInText(Pattern, Text, d): # tool for checking the existance of a pattern in a sequence
    k = len(Pattern) # setting pattern length as k
    for i in range(len(Text) - k + 1): # start searching
        if HammingDistance(Pattern, Text[i:i+k]) <= d:
            return True # if HammingDistance is d -> true
    return False

def MotifEnumeration(Dna, k, d): 
    Patterns = set()
    # check first sequence's patterns as k=mers
    for i in range(len(Dna[0]) - k + 1):
        pattern = Dna[0][i:i+k]
        # generate every neighbor of k-mer
        for neighbor in Neighbors(pattern, d):
            # check if that neighbor is in every line
            if all(IsPatternInText(neighbor, strand, d) for strand in Dna):
                Patterns.add(neighbor)
    return Patterns

result = MotifEnumeration(DNA, k, d)
print(" ".join(sorted(result)))
