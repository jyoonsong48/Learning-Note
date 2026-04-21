import re

#with open("rosalind_sseq.txt", 'r', encoding='utf-8') as f:
#   data = f.read()
data = """insert sequences here"""

str = data.split(">")
seq_n_pattern = [item for s in str for item in re.split(r'Rosalind_\d\d+', s) if item]
seq_n_pattern = [s.replace('\n', '') for s in seq_n_pattern if s.strip()]

str1 = seq_n_pattern[0]
str2 = seq_n_pattern[1]

def difference(p,q):
    location = []
    for i in range(len(p)): 
        if p[i] != q[i]:
            location.append(i)
    return location

def trans(ls, p, q):
    transition = 0
    transversion = 0
    for i in ls:
        if {p[i], q[i]} == {"A", "G"} or {p[i], q[i]} == {"C", "T"}:
            transition = transition + 1
        else:
            transversion = transversion + 1
    total = transition / transversion
    return total


print(round(trans(difference(str1, str2), str1, str2), 11))
