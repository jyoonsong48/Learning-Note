import re
with open("rosalind_trie.txt", 'r', encoding='utf-8') as f:
    dataset = f.read()

data = dataset.strip().split("\n")

bases = []

for d in data:
    char = list(d)
    bases.append(char)


# each node -> dict.: {char: next node #}
# (start root=1)

trie = {1: {}}   # root: no edge
next_node_id = 2  # node #
root = 1

for base in bases:
    current = root
    for char in base:
        if char in trie[current]:
            current = trie[current][char]   # follow (if can)
        else:
            new_node = next_node_id
            trie[new_node] = {}              # ① new node
            trie[current][char] = new_node   # ② parent -> new node edge
            next_node_id += 1                # ③ +1
            current = new_node

"""for key, value in trie.items():
    if value:
        for k, v in value.items():
            print(key, v, k)"""                          
        
with open("TRIE_answer.txt", "w") as f:
    for key, value in trie.items():
        if value:
            for k, v in value.items():
                print(key, v, k, file=f)