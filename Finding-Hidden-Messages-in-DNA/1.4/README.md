### $\color{#fffff}{\text{1.4: Finding Patterns Forming Clumps in a DNA Sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.4
# By: Jiyoon Song
# Content: Finding patterns forming clumps in a sequence
# ==========================================================

  def FrequencyTable(text, k):
    counts = {} # empty dictionary
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        if pattern in counts:
            counts[pattern] = counts[pattern] + 1
        else:
            counts[pattern] = 1
            
    return counts

def FindClumps(Text, k, L, t):
    Patterns = []
    n = len(Text)
    
    for i in range(n - L + 1):
        Window = Text[i : i + L]
        freqMap = FrequencyTable(Window, k)
        
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.append(s)
                
    # set : remove duplicates
    return list(set(Patterns))

# RUN
genome = "" # insert sequence here
results = FindClumps(genome, k, L, t) # insert k. L, t here / k: Pattern length, L: desired clump length, t: minimal frequency / cf. in bacteria: typically k=9, L=500, t=3
print(*results)

<b></b>
</pre> 
</details>
