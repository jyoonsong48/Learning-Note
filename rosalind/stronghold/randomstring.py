import math

dataset = """sequence and numbers"""

data = dataset.split(" ")
sequence = data[0]
del data[0]
data = list(map(float, data))

n_at = sequence.count("A") + sequence.count("T")
n_cg = sequence.count("C") + sequence.count("G")

numbers = []
for x in data:
    percent = (n_cg) * math.log10(x/2) + (n_at) * math.log10((1-x)/2)
    numbers.append(round(percent, 3))

print(*numbers)