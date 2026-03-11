### $\color{#fffff}{\text{1.2: Finding Certain Regulatory Sequences/k-mer in DNA sequence}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.2
# By: Jiyoon Song
# Content: Finding k-mer/regulatory sequence
# ==========================================================

text = "" # sequence
pattern = "" # pattern

def pattern_count(text, pattern):
    count = 0
    # len() -> function for counting length.
    # range(start, end) -> repeat*(|end-start|)
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count = count + 1
    return count

print(f"Number of '{pattern}' found in '{text}': {pattern_count(text, pattern)}")

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

text = "" # fuil sequence here
k =  # insert the length of k-mer you want to find / cf. bacterial DnaA boxes are usually 9 nt long
counts = {} # this will be the dictionary

for i in range(len(text) - k + 1): # we don't need to count the last letter of the sequence, for example. (i.e. It's pointless to count from the 9th letter of a 10-letter-sequence if the pattern is 3 nt long)
	pattern = text[i : i  + k]
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

# for: finding most frequnet patterns in certain length
<b></b>
</pre> 
</details>
