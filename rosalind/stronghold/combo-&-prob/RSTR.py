dataset = """number of generated seq, GC contect, target seq"""

data = dataset.split()

n, x, s = int(data[0]), float(data[1]), data[2]

probablity = 1
for char in s:
    if char == "A" or char == "T":
        probablity = probablity * (1-x)/2
    else:
        probablity = probablity * x/2

prob = 1 - (1 - probablity) ** n

print(prob)