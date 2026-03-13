### $\color{#fffff}{\text{1.8: Hamming Distance Between Two DNA Sequences}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.8
# By: Jiyoon Song
# Content: Hamming distance between two strings
# ==========================================================

p = "" # first sequence
q = "" # second sequence

def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): # start matching from the first letter
        if p[i] != q[i]: dist += 1 # if diff. -> add 1 to distance
        else: dist = dist + 0
    return dist

print(HammingDistance(p,q))
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.8: Finding All Approximate Occurrences of a Pattern in a DNA sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.8
# By: Jiyoon Song
# Content: Finding all approximate occurrences of a pattern in a string
# ==========================================================

sequence = "" # insert sequence here
pattern = "" # insert pattern here
d =  # insert maximum permissible error count
def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): # start matching from the first letter
        if p[i] != q[i]: dist += 1 # if diff. -> add 1 to distance
        else: dist = dist + 0
    return dist
positions = [] # generate a dictionary
for i in range(len(sequence) - len(pattern) + 1): # count from the first letter - (pattern + 1)th letter
        current_window = sequence[i : i + len(pattern)] # now counting...
        if HammingDistance(current_window, pattern) <= d: # if hamming distance is smaller than d:
            positions.append(i) # add the location to the dictionary
print(*positions)
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.8: Finding All (including errors) Occurrences of a Pattern in a DNA sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.8
# By: Jiyoon Song
# Content: Finding all (including errors) occurrences of a pattern in a string
# ==========================================================

sequence = "" # insert sequence here
pattern = "" # insert pattern here
d =  # insert maximum permissible error count

def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): # start matching from the first letter
        if p[i] != q[i]: dist += 1 # if diff. -> add 1 to distance
        else: dist = dist + 0
    return dist

def ApproxHammingCount(sequence, pattern):
    count = 0
    for i in range(len(sequence) - len(pattern) + 1):
        current_window = sequence[i : i + len(pattern)] # now counting...
        if HammingDistance(current_window, pattern) <= d:
            count += 1
    return count

print(ApproxHammingCount(sequence,pattern))
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.8: Finding All Patterns (with Mismatches) in a DNA sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.8
# By: Jiyoon Song
# Content: Finding all frequent words with mismatches problem
# ==========================================================

sequence = "" # insert sequence here
pl =  # insert desired length of pattern here
d = # insert maximum value of error permissible
def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): # start matching from the first letter
        if p[i] != q[i]: dist += 1 # if diff. -> add 1 to distance
        else: dist = dist + 0
    return dist
def Neighbors(Pattern, d): # define "neighbors" -> generating a pattern length of 'pl' with 'd' amount of error
    if d == 0: # if there's no 'error'
        return {Pattern}
    if len(Pattern) == 1: # if there's 'error' (difference)
        return {'A', 'C', 'G', 'T'} # possible 'error' options
    
    neighborhood = set() # remove duplicates
    suffix_neighbors = Neighbors(Pattern[1:], d) # finding neighbors of the suffix (except the first letter)
    for neighbor in suffix_neighbors: # compare found neightbors & origin
        if HammingDistance(Pattern[1:], neighbor) < d: # if the difference is smaller than d
            for base in ['A', 'C', 'G', 'T']: # any base can be used for the first letter
                neighborhood.add(base + neighbor) # so add it!
        else:
            neighborhood.add(Pattern[0] + neighbor) # if the difference is d
    return neighborhood # return it (cannot change the first letter)
def FrequentWordsWithMismatches(text, k, d): # finding the most frequent pattern
    freq_map = {} # empty dictionary (frequency map/k-mer index)
    for i in range(len(text) - k + 1): # scan through : 1 - (sequence - pl + 1)
        pattern = text[i:i+k] # the part python is currently looking at
        neighborhood = Neighbors(pattern, d) # generate every possible pattern (neighbors)
        for neighbor in neighborhood: # put generated neighbors in the dictionary
            if neighbor not in freq_map:
                freq_map[neighbor] = 1 # add 1 when it's not on the list
            else:
                freq_map[neighbor] += 1 # when it's on the list -> +1
    max_count = max(freq_map.values()) # count the most frequent patterns
    result = [kmer for kmer, count in freq_map.items() if count == max_count] # result = if it's most frequent -> add it to the dictionary
    return result # return the result

final_result = FrequentWordsWithMismatches(sequence, pl, d) # cleaning up --> put it into final_result (not necessary)
print(*final_result) # result :)
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.8: Finding the Most Frequent k-mers (with mismatches and reverse complements) in a DNA Sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.8
# By: Jiyoon Song
# Content: Finding the most frequent k-mers (with mismatches and reverse complements) in a string
# ==========================================================

sequence = "" # insert sequence here
pl =  # insert desired length of pattern here
d =  # insert maximum permissble error count here
# cf. for most bacteria: pl=9, d=1 or 2
def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): # start matching from the first letter
        if p[i] != q[i]: dist += 1 # if diff. -> add 1 to distance
        else: dist = dist + 0
    return dist

def Neighbors(Pattern, d): # define "neighbors" -> generating a pattern length of 'pl' with 'd' amount of error
    if d == 0: # if there's no 'error'
        return {Pattern}
    if len(Pattern) == 1: # if there's 'error' (difference)
        return {'A', 'C', 'G', 'T'} # possible 'error' options
    
    neighborhood = set() # remove duplicates
    suffix_neighbors = Neighbors(Pattern[1:], d) # finding neighbors of the suffix (except the first letter)
    for neighbor in suffix_neighbors: # compare found neightbors & origin
        if HammingDistance(Pattern[1:], neighbor) < d: # if the difference is smaller than d
            for base in ['A', 'C', 'G', 'T']: # any base can be used for the first letter
                neighborhood.add(base + neighbor) # so add it!
        else:
            neighborhood.add(Pattern[0] + neighbor) # if the difference is d
    return neighborhood # return it (cannot change the first letter)

def Reverse_Complement(pattern):
    pairs = {"A":"T", "T":"A", "C":"G", "G":"C"} # A-T & G-C
    Complement = ""
    for base in pattern:
        Complement = Complement + pairs[base] # complementary strand sequence generated
    return Complement[::-1] # reversing the order

def FrequentWordsWithMismatchesandRC(text, k, d): # finding the most frequent pattern & also the reversed ones!!
    freq_map = {} # empty dictionary (frequency map/k-mer index)
    for i in range(len(text) - k + 1): # scan through : 1 - (sequence - pl + 1)
        pattern = text[i:i+k] # the part python is currently looking at
        neighborhood = Neighbors(pattern, d) # generate every possible pattern (neighbors)
        for neighbor in neighborhood: # put generated neighbors in the dictionary
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
    combined_freq = {} # new dictionary: original + reversed complementary
    for kmer in freq_map:
        rc_kmer = Reverse_Complement(kmer) # generate reversed complementary (RC) sequences
        combined_freq[kmer] = freq_map.get(kmer, 0) + freq_map.get(rc_kmer, 0) # combine OG + RC frequency
    max_count = max(combined_freq.values()) # find highest frequency
    result = [kmer for kmer, count in combined_freq.items() if count == max_count] # collect highest-frequency-patterns
    return result

final_result = FrequentWordsWithMismatchesandRC(sequence, pl, d)
print(*final_result)
<b></b>
</pre> 
</details>
