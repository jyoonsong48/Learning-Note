### $\color{#fffff}{\text{1.3: Some Hidden Messages are More Surprising than Others}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.3
# By: Jiyoon Song
# Content: Generating complementary strand of a sequence
# ==========================================================
  
pairs = {"A":"T", "T":"A", "C":"G", "G":"C"} # A-T & G-C

DNA = ""  # insert sequence here
Complement = ""

for base in DNA:
    Complement = Complement + pairs[base] # complementary strand sequence generated

Reverse_Complement = Complement[::-1] # 5' to 3' end! / ::-1 -> revese from :(start):(end)-1(backwards)

print(Reverse_Complement)
# for: generating a reversed sequence with complementary base
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{1.3: Some Hidden Messages are More Surprising than Others}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>Python</b>
# ==========================================================
# Project: Finding Hidden Messages in DNA 1.3
# By: Jiyoon Song
# Content: Finding locations of certain pattern in a sequence
# ==========================================================

  sequence = "" # insert DNA sequence "here"
pattern = "" # insert pattern "here"

positions = []
for i in range(len(sequence) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:  
            positions.append(i) # finding 'position' of the pattern

print(*positions)
# for: finding certain pattern's locations in a sequence
<b></b>
</pre> 
</details>
