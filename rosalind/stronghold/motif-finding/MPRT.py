import re
import requests
from bs4 import BeautifulSoup

with open("insert file path here", 'r', encoding='utf-8') as f:
    dataset = f.read()



ID_raw = dataset.split("\n")
ID = [i.split("_")[0] for i in ID_raw]

fasta = []
for i in range(len(ID)):
    url = f'https://www.uniprot.org/uniprot/{ID[i]}.fasta'
    response = requests.get(url)
    html = response.text
    if response.status_code == 200:
        fasta_data = response.text
        fasta.append(fasta_data)
    else:
        print("Couldn't get the sequence")

protein_sequence = []
for i in range(len(fasta)):
    protein = fasta[i]
    protein = protein.split("\n")
    del protein[0]
    protein_seq = "".join(protein)
    protein_sequence.append(protein_seq)
    
results = {}
key = []
for i in range(len(protein_sequence)):
    looking = protein_sequence[i]
    match = re.findall(r'(?=N[^P][ST][^P])', looking)
    if match:
        locations = [m.start() + 1 for m in re.finditer(r'(?=N[^P][ST][^P])', looking)]
        results[ID_raw[i]] = locations
print(results)


with open("uniprot_mortif_location.txt", "w") as f:
    for idx, (id, locations) in enumerate(results.items()):
        if idx == 0:
            f.write(id)
        else:
            f.write(f"\n{id}")
        for jdx, item in enumerate(locations):
            if jdx == 0:
                f.write(f"\n{item}")
            else:
                f.write(f" {item}")