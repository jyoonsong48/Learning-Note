from collections import deque
import re

dataset = """(cat)dog;
dog cat

(dog,cat);
dog cat"""

dataset = dataset.split("\n")
data = []
temp = []
for item in dataset:
    if item == "":
        data.append(temp)
        temp = []
    else:
        temp.append(item)
data.append(temp)

# NEEDS TO BE DUBUGGED
def parse(newick_str):
    graph = {}
    stack = [] 
    current_name = ""
    anon_count = [0]

    def get_anon():
        anon_count[0] += 1
        return f"anon_{anon_count[0]}"
    def add_edge(a, b):
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    def connect_parent_to_children(parent, children):
        for child in children:
            if type(child) == str:
                add_edge(parent, child)
            if type(child) == list:
                anon = get_anon()
                add_edge(parent, anon)
                connect_parent_to_children(anon, child)
        pass

    for n in newick_str:
        if n == '.':
            continue
        if n in "();,":
            if current_name:
                stack.append(current_name)
                current_name = ""
            else:
                if n == "," or n == ")":

                    if stack and not isinstance(stack[-1], list) and stack[-1] != "(":
                        stack.append(get_anon())
            if n == "(":
                stack.append(n)
            elif n == ")":
                if current_name:
                    stack.append(current_name)
                    current_name = ""
                
                leaf= []
                while stack[-1] != "(":
                    leaf.append(stack.pop())
                stack.pop()
                stack.append(leaf)
            elif n == ",":
                pass
            elif n == ";":
                top = stack.pop()
                if isinstance(top, list):
                    parent = "anonymous_root"
                    children = top
                else:
                    parent = top
                    children = stack.pop()
                connect_parent_to_children(parent, children)

        else:
            current_name += n

    return graph

def bfs(x, y, graph):
    queue = deque([x])
    visited = set([x])
    dist = {x: 0}
    
    while queue:
        current_node = queue.popleft()

        if current_node == y:
            return dist[current_node]

        for next_node in graph[current_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                dist[next_node] = dist[current_node] + 1

    return -1

answer = []
for d in data:
    x, y = d[1].split(" ")
    graph = parse(d[0])
    answer.append(bfs(x, y, graph))

print(*answer)