### $\color{#fffff}{\text{2.4: Finding a Median String}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.4
# By: Jiyoon Song
# Content: Finding a median string
# ==========================================================

k =  # insert pattern length here
DNA = [] # insert DNA strings here
import math
def HammingDistance(p, q):
    return sum(1 for i in range(len(p)) if p[i] != q[i]) # if there's a difference -> +1 (sum)
 
def DistanceBetweenPatternAndStrings(Pattern, DNA):
    k = len(Pattern)
    total_distance = 0
    for text in DNA:
        min_hamming = math.inf
        for i in range(len(text) - k + 1):
            d = HammingDistance(Pattern, text[i:i+k])
            if min_hamming > d:
                min_hamming = d
        total_distance += min_hamming
    return total_distance

def AllPossibleKmers(k): # generate all possible k-mers
    if k == 1: return ['A', 'C', 'G', 'T'] # base case: prevent error
    return [base + suffix for base in ['A', 'C', 'G', 'T'] for suffix in AllPossibleKmers(k-1)] # recursive : put k-1 suffix to A, C, G, T

def MedianString(DNA, k):
    distance = math.inf # resetting
    median = "" # varaiable to save "best" pattern
    for pattern in AllPossibleKmers(k): # for every possible k-mers,
        d = DistanceBetweenPatternAndStrings(pattern, DNA) # calculation
        if distance > d: # if current distance is smaller than original -> update
            distance = d # that will be the best match
            median = pattern # save the best match
            
    return median # result: bring out the "most" best match

print(MedianString(DNA, k))
