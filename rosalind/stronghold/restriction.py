with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

dataset = data.split("\n")
del dataset[0]
DNA = ''.join(dataset)

def complement(str):
    replace = str.maketrans('ACGT', 'TGCA')
    complement = str.translate(replace)
    complement = complement[::-1]
    return complement

location_length = []
for i in range(len(DNA)):
    for j in range(4, 13):
        if i + j > len(DNA):
            break
        window = DNA[i:i+j]
        if window == complement(window):
            location_length.append((i+1, len(window)))
        
# print(location_length, sep="\n")


with open("restriction_site.txt", "w") as f:
    for key,value in location_length:
        f.write(f"{key} {value}\n")

            



