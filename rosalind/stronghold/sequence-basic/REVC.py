DNA = "DNA sequence here"

replace = DNA.maketrans('ACGT', 'TGCA')
complement = DNA.translate(replace)
complement = complement[::-1]
print(complement)