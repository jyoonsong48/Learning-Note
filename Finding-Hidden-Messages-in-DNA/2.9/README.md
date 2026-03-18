### $\color{#fffff}{\text{2.9: Implementing GibbsSampler}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.9
# By: Jiyoon Song
# Content: Implement GibbsSampler
# ==========================================================

k =  # insert k-mer length here
t = # insert number of strings here
N = # insert repeating time of GibbsSampler here
DNA = [] # insert sequences of DNA here

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

def Score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    total_score = 0
    for j in range(k):
        column = [motifs[i][j] for i in range(t)]
        counts = {
            'A': column.count('A'),
            'C': column.count('C'),
            'G': column.count('G'),
            'T': column.count('T')
        }
        max_count = max(counts.values())
        score_for_this_column = t - max_count
        total_score += score_for_this_column
    return total_score

def make_profile(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = {
        'A': [0.0] * k, 'C': [0.0] * k, 'G': [0.0] * k, 'T': [0.0] * k
    }
    for j in range(k):
        column = [motif[j] for motif in motifs]
        profile['A'][j] = (column.count('A') + 1) / (t + 4)
        profile['C'][j] = (column.count('C') + 1) / (t + 4)
        profile['G'][j] = (column.count('G') + 1) / (t + 4)
        profile['T'][j] = (column.count('T') + 1) / (t + 4)
    return profile

import random

def ProfileRandomKmer(text, profile, k):
    kmers = [] # empty list: for k-mer
    weights = [] # empty list: for probability calculated from profile
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k] # slicing
        kmers.append(kmer) # add sliced k-mer into the list
        weights.append(ProfileProb(kmer, profile)) # add the profile of sliced k-mer into the list
    return random.choices(kmers, weights=weights)[0] # choose random k-mer based on probability (weighted selection)


def GibbsSampler(DNA, k, t, N):
    motifs = [] # motif list
    for text in DNA: # for a string of DNA:
        start = random.randint(0, len(text) - k) # choose random starting point
        motifs.append(text[start:start+k]) # from that point -> slicing
    
    best_motifs = list(motifs)
    for _ in range(N): # repeating N times (local optimisation)
        i = random.randint(0, t - 1)
        motifs_except_i = motifs[:i] + motifs[i+1:] # generate list except itself (i) 
        profile = make_profile(motifs_except_i) 
        motifs[i] = ProfileRandomKmer(DNA[i], profile, k)
        if Score(motifs) < Score(best_motifs):
            best_motifs = list(motifs)
            
    return best_motifs
def RepeatedGibbsSearch(DNA, k, t, N, restarts=100): # to avoid local optima -> repeat GibbsSmapler 'restarts' time (you can change the value)
    best_final_motifs = []
    min_score = math.inf # resetting
    
    print(f"Starting {restarts} Gibbs Sampler runs...") # Indicator
    
    for i in range(restarts):
        current_run = GibbsSampler(DNA, k, t, N)
        current_score = Score(current_run)  # calculate Score
        if current_score < min_score: # if current Score is lower than saved minimum:
            min_score = current_score # update minimum Score
            best_final_motifs = current_run # update best_final_motifs to current moti
            print(f"Run {i+1}: New best score found! -> {min_score}") # Indicatior
            
    return best_final_motifs
print(*RepeatedGibbsSearch(DNA, k, t, N, 100))

