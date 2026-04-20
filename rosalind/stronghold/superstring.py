import re

with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()

sequences = []
current = ""
for line in dataset.split("\n"):
    if line.startswith(">"):
        if current:
            sequences.append(current)
        current = "" 
    else:
        current += line.strip()

sequences.append(current)

superstring = {}

def supersuperstring(str1, str2):
    for i in range(len(str2), int(0.5*len(str2)), -1):
        if str1.endswith(str2[:i]):
            return str1+str2[i:]
    return None

def search(ls):
    for str1 in sequences:
        for str2 in sequences:
            if str1 != str2:
                supersuperstring(str1, str2)
                if supersuperstring(str1, str2):
                    superstring[str1] = str2
    return superstring

def merging(dict):
    key = [k for k in dict if k not in dict.values()][0]
    current = [k for k in dict if k not in dict.values()][0]
    while key in dict:
        next = dict[key]
        key = next
        current = supersuperstring(current, next)
    return current

def main(ls):
    return merging(search(ls))

result = main(sequences)

with open("superstring.txt", "w") as f:
    f.write(result)
