import re
with open("rosalind_sort.txt", 'r', encoding='utf-8') as f:
    dataset = f.read()

A, B= dataset.strip().split("\n")
A = tuple(int(x) for x in re.findall(r'\d+', A))
B = tuple(int(x) for x in re.findall(r'\d+', B))


def neighbour(x): 
    n = len(x)
    result = []
    for i in range(n):
        for j in range(i+1, n):
            reverse_x = x[:i] + x[i:j+1][::-1] + x[j+1:]
            reversal = (i+1, j+1) #1-indexed for humans
            result.append((reverse_x, reversal))
    return result

visited_x = {A: (0, None, None)}
visited_y = {B: (0, None, None)}
que_x = [A]
que_y = [B]
intersection = None

while intersection == None: # finding intersection
    if len(que_x) <= len(que_y):
        extend_que, extend_visited, reverse_visited = que_x, visited_x, visited_y
        direction = 'x'
    else:
        extend_que, extend_visited, reverse_visited = que_y, visited_y, visited_x
        direction = 'y'
# smaller queue gets expanded (x -> y -> x -> y ... : usually)
    next_lvl = []
    found = False

    for current_node in extend_que:
        dist = extend_visited[current_node][0]
        for neighbour_node, reversal in neighbour(current_node):
            if neighbour_node in extend_visited:
                continue
            extend_visited[neighbour_node] = (dist+1, current_node, reversal)
            next_lvl.append(neighbour_node)
            if neighbour_node in reverse_visited:
                intersection = neighbour_node
                found = True
                break # (breaking from for loop)
        if found:
            break # if intersection -> stop searching (intersection != None)

    if direction == 'x':
        que_x = next_lvl
    else:
        que_y = next_lvl

# visited_x[permutation] = (distance, parent permutation, parent-> permutation reversal)

path_x = []              # reversals
node = intersection       # start from intersection node

while node != A:          # until π (start)
    dist, parent, reversal = visited_x[node]
    path_x.append(reversal)
    node = parent 
    if node == A:
        break

path_y = []
node = intersection

while node != B: # same! but until γ (end)
    dist, parent, reversal = visited_y[node]
    path_y.append(reversal)
    node = parent
    if node == B:
        break


path_x.reverse()          # π → ... → intersection
final_path = path_x + path_y   # π → ... → intersection → ... → γ

total_dist = visited_x[intersection][0] + visited_y[intersection][0]
print(total_dist)
for r in final_path:
    print(*r)