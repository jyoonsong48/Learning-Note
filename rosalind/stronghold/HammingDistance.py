# file:
with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()
# OR
# data = """
# insert sequences separated by \n here
# """
sequences = data.split("\n")
p = sequences[0]
q = sequences[1]
def HammingDistance(p,q):
    dist = 0 # start from 0
    for i in range(len(p)): 
        if p[i] != q[i]: dist += 1 
        else: dist = dist + 0
    return dist

print(HammingDistance(p,q))