from monoisotopic_mass_table import mass_table
import re
with open("rosalind_spec.txt", 'r', encoding='utf-8') as f:
    dataset = f.read()

data = dataset.strip().split("\n")

mass = []
for i in range(len(data)):
    if i >= 1:
        m = float(data[i]) - float(data[i-1])
        mass.append(m)

tolerance = 1
def find_protein(mass_value, mass_table, tol):
    matches = [(k, abs(mv - mass_value)) for k, mv in mass_table.items() if abs(mv - mass_value) <= tol]
    if not matches:
        return None
    return min(matches, key=lambda pair: pair[1])[0]

result = [find_protein(mv, mass_table, tolerance) for mv in mass]
protein = "".join(result)

print(protein)