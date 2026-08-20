with open("insert file path here", 'r', encoding='utf-8') as f:
    data = f.read()

numbers = data.split(" ")

k = int(numbers[0]) # AA
m = int(numbers[1]) # Aa
n = int(numbers[2]) # aa
# OR enter manually
"""
k =
m = 
n =
"""
total = k+m+n
total_prob = total * (total-1)

m_m = m * (m-1) * 0.25
m_n = m * n
n_n = n * (n-1)

aa_prob = m_m + m_n + n_n

prob = 1 - (aa_prob / total_prob)

print(prob)

