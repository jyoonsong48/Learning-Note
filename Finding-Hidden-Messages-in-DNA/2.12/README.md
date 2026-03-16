### $\color{#fffff}{\text{2.12: Implement Distance Between Pattern And Strings}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.12
# By: Jiyoon Song
# Content: Implementing Distance Between Pattern And Strings
# ==========================================================

Pattern = "" # insert pattern here
DNA = [] # insert DNA strings here
import math
def HammingDistance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def DistanceBetweenPatternAndStrings(Pattern, DNA):
    k = len(Pattern) # k = pattern length
    distance = 0 # reset distance
    for text in DNA: # for each string,
        mindist = math.inf # set minimum distance as infinity (resetting)
        for i in range(len(text) - k + 1): # check every possible k-mer location
            current_kmer = text[i:i+k] # at current location -> slice into k-length (k-mer)
            d = HammingDistance(Pattern, current_kmer) 
            if mindist > d: # if current distance is smaller than origianl minimum,
                mindist = d # current distance will be the best match
        distance += mindist # every minimum from every string collected
    return distance # sum of minimum distances

print(DistanceBetweenPatternAndStrings(Pattern, DNA))
