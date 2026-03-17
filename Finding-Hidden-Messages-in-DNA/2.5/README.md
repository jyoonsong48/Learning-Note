### $\color{#fffff}{\text{2.5: Calculating Probability}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.5
# By: Jiyoon Song
# Content: Calculating probability
# ==========================================================
profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
} # insert strings' profile here
kmer = "" # insert kmer to calculate profile probability here
def ProfileProb (kmer, profile):
    prob = 1.0 # resetting
    for i in range(len(kmer)):
        nucleotide = kmer[i] # in a kmer, nucleotide is a base you're looking at right now
        p = profile[nucleotide][i] # p is that base's profile value
        prob *= p # probability => multiplying that p values (cumulative probability calculation)
    return prob

print(ProfileProb(kmer, profile))
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{2.5: Finding a Profile-most Probable K-mer in a String}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.5
# By: Jiyoon Song
# Content: Finding a Profile-most probable k-mer in a string
# ==========================================================
profile = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
} # insert strings' profile here
kmer = "" # insert kmer to calculate profile probability here
def ProfileProb (kmer, profile):
    prob = 1.0 # resetting
    for i in range(len(kmer)):
        nucleotide = kmer[i] # in a kmer, nucleotide is a base you're looking at right now
        p = profile[nucleotide][i] # p is that base's profile value
        prob *= p # probability => multiplying that p values (cumulative probability calculation)
    return prob

print(ProfileProb(kmer, profile))
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{2.5: Implementing GreedyMotifSearch}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.5
# By: Jiyoon Song
# Content: Implementing GreedyMotifSearch
# ==========================================================
k = # insert k-mer length here
t =  # insert 
DNA = [] # insert DNA sequences here
import math
def HammingDistance(p, q):
    return sum(1 for i in range(len(p)) if p[i] != q[i])
 
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

def ProfileProb (kmer, profile):
    prob = 1.0
    for i in range(len(kmer)):
        nucleotide = kmer[i]
        p = profile[nucleotide][i]
        prob *= p
    return prob

def ProfileMostProb (DNA, profile, k):
    max_prob = -1
    MostProbableKmer = ""
    for i in range(len(DNA) - k + 1):
        current_kmer = DNA[i:i+k]
        current_prob = ProfileProb(current_kmer, profile)
        if current_prob > max_prob:
            max_prob = current_prob
            MostProbableKmer = current_kmer
    return MostProbableKmer

def Score(motifs): # calculating score (calculate total mismatch score)
    k = len(motifs[0])
    t = len(motifs)
    total_score = 0 # resetting
    for j in range(k):
        column = [motifs[i][j] for i in range(t)] # for each string:
        counts = {
            'A': column.count('A'),
            'C': column.count('C'),
            'G': column.count('G'),
            'T': column.count('T')
        } # count each base
        max_count = max(counts.values()) # maximum values
        score_for_this_column = t - max_count # score = string length - maximum value
        total_score += score_for_this_column
    return total_score

def make_profile(motifs): # generating motif
    t = len(motifs)
    k = len(motifs[0])
    profile = {
        'A': [0.0] * k, 'C': [0.0] * k, 'G': [0.0] * k, 'T': [0.0] * k
    } # blank
    for j in range(k):
        column = [motif[j] for motif in motifs]
        profile['A'][j] = column.count('A') / t
        profile['C'][j] = column.count('C') / t
        profile['G'][j] = column.count('G') / t
        profile['T'][j] = column.count('T') / t # calculating probability 
    return profile

def GreedyMotifSearch (DNA, k, t):
    best_motifs = [text[:k] for text in DNA] # will be the result
    first_string = DNA[0]
    for i in range(len(first_string)-k + 1):
        Motif1 = first_string[i:i+k] # slicing
        current_motifs = [Motif1]
        for j in range(1, t): # for that sliced k-mer:
            curr_profile = make_profile(current_motifs) 
            next_motif = ProfileMostProb(DNA[j], curr_profile, k)
            current_motifs.append(next_motif) # calculating profile, motif -> add them
        if Score(current_motifs) < Score(best_motifs): # if the score is samller:
            best_motifs = current_motifs # update!
    return best_motifs

print(*GreedyMotifSearch(DNA, k, t))
<b></b>
</pre> 
</details>
