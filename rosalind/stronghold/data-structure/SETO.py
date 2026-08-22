import re
with open("rosalind_seto.txt", 'r', encoding='utf-8') as f:
    dataset = f.read()

n, A, B= dataset.split("\n")
U = list(range(1, int(n)+1))
A = list(map(int, re.findall(r'\d+', A)))
B = list(map(int, re.findall(r'\d+', B)))

# AuB
A_B = A + B
AuB = set(A_B)

A_set = set(A)
B_set = set(B)

AB = [x for x in A if x not in B_set]
BA = [x for x in B if x not in A_set]
Ac = [x for x in U if x not in A_set]
Bc = [x for x in U if x not in B_set]

# AnB
AnB = [x for x in AuB if x not in AB]
AnB = [x for x in AnB if x not in BA]

# for writing
def fmt(s):
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}"

with open("SETO.txt", "w") as f:
    f.write(fmt(AuB) + "\n")
    f.write(fmt(AnB) + "\n")
    f.write(fmt(AB) + "\n")
    f.write(fmt(BA) + "\n")
    f.write(fmt(Ac) + "\n")
    f.write(fmt(Bc))