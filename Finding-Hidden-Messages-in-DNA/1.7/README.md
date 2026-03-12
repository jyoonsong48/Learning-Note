### $\color{#fffff}{\text{1.7: Generating a Skew Diagram}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.7
# By: Jiyoon Song
# Content: Generating a skew diagram from a sequence
# ==========================================================

Genome = "" # insert genome sequence here

def SkewDiagram(Genome):
    skew = [0] # start value = 0
    for base in Genome:
        current_score = skew[-1] # -1 : not a value! refering to a value right before
        if base == "G":
            new_score = current_score + 1
        elif base == "C":
            new_score = current_score - 1
        else:
            new_score = current_score + 0
        skew.append(new_score) # add new score
        
    return skew 
print(*SkewDiagram(Genome)) # print the data
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.7: Finding a Position in a Genome Where the Skew Diagram Attains a Minimum}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.7
# By: Jiyoon Song
# Content: Finding a postion of a skew diagram's minimum
# ==========================================================

Genome = "" # insert genome sequence here

def SkewDiagram(Genome):
    skew = [0] # start value = 0
    for base in Genome:
        current_score = skew[-1] # -1 : not a value! refering to a value right before
        if base == "G":
            new_score = current_score + 1
        elif base == "C":
            new_score = current_score - 1
        else:
            new_score = current_score + 0
        skew.append(new_score) # add new score
        
    return skew 
print(*SkewDiagram(Genome)) # print the data
<b></b>
</pre> 
</details>
