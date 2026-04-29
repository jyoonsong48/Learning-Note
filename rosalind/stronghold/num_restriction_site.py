import re
dataset = """807203
TCTCAGTTG
0.000 0.064 0.134 0.203 0.238 0.278 0.342 0.412 0.422 0.497 0.530 0.583 0.640 0.725 0.742 0.791 0.858 0.931 1.000"""

data = dataset.split("\n")
n = int(data[0])
s = data[1]
num = [float(x) for x in data[2].split()]

def gc_cont(s, num):
    content = 1
    for char in s:
        if char == "A" or char == "T":
            content *= (1-num) / 2
        else:
            content *= (num) / 2
    return content

def site(n, s, num):
    prob = (n - len(s) + 1) * gc_cont(s, num)
    return prob

num_restriction_site = [round(site(n, s, gc), 3) for gc in num]

print(*num_restriction_site)
