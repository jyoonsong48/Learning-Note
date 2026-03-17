### $\color{#fffff}{\text{2.6: Implement GreedyMotifSearch with Pseudocounts}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 2.6
# By: Jiyoon Song
# Content: Implementing GreedyMotifSearch with Pseudocounts
# ==========================================================

k = # insert k-mer length here
t =  # insert total string number
DNA = [] # insert DNA sequences here
DNA = classify_dna(user_input)
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
        profile['A'][j] = column.count('A') + 1 / t + 4
        profile['C'][j] = column.count('C') + 1/ t + 4
        profile['G'][j] = column.count('G') + 1/ t + 4
        profile['T'][j] = column.count('T') + 1/ t + 4
    return profile
# if probability = 0 -> error!! => add +1 for each count (pseudocounts) to prevent error

def GreedyMotifSearch (DNA, k, t):
    BestMotifs = []
    best_motifs = [text[:k] for text in DNA]
    first_string = DNA[0]
    for i in range(len(first_string)-k + 1):
        Motif1 = first_string[i:i+k]
        current_motifs = [Motif1]
        for j in range(1, t):
            curr_profile = make_profile(current_motifs)
            next_motif = ProfileMostProb(DNA[j], curr_profile, k)
            current_motifs.append(next_motif)
        if Score(current_motifs) < Score(best_motifs):
            best_motifs = current_motifs
    return best_motifs

print(*GreedyMotifSearch(DNA, k, t))
