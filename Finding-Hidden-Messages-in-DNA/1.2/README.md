### $\color{#fffff}{\text{1.2: Finding Certain Regulatory Sequences/k-mer in DNA sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.2
# By: Jiyoon Song
# Content: Finding k-mer/regulatory sequence
# ==========================================================

sequence = "" # insert sequence here
pattern = "" # insert pattern here

def pattern_count(sequence, pattern):
    count = 0
    # len() -> function for counting length.
    # range(start, end) -> repeat*(|end-start|)
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i : i + len(pattern)] == pattern:
            count = count + 1
    return count

print(f"Number of '{pattern}' found in '{sequence}': {pattern_count(sequence=, pattern)}")

# for: finding regulatory sequences, k-mers
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.2: Finding Most Frequent Patterns in Certain Length in DNA Sequences}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.2
# By: Jiyoon Song
# Content: Finding most frequent patterns
# ==========================================================

sequence = "" # fuil sequence here
k =  # insert the length of k-mer you want to find / cf. bacterial DnaA boxes are usually 9 nt long
counts = {} # this will be the dictionary

for i in range(len(sequence) - k + 1): # we don't need to count the last letter of the sequence, for example. (i.e. It's pointless to count from the 9th letter of a 10-letter-sequence if the pattern is 3 nt long)
	pattern = sequence[i : i  + k]
	if pattern in counts:
		counts[pattern] = counts[pattern] + 1
	else:
		counts[pattern] = 1 # self-explanatory

# counting the MOST frequent pattern

max_count = max(counts.values())
frequent_patterns = []
for pattern in counts:
	if counts[pattern] == max_count:
		frequent_patterns.append(pattern)

print("Most frequent pattern(s)", frequent_patterns)
<b></b>
</pre> 
</details>
