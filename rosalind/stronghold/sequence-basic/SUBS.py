with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

dataset = data.split("\n")
sequence = dataset[0]
pattern = dataset[1]

positions = []
for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i : i + len(pattern)] == pattern:  
            positions.append(i+1) # finding 'position' of the pattern

print(*positions)