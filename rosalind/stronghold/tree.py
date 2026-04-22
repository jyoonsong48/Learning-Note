dataset = """insert dataset here"""

data = dataset.split("\n")
nodes = int(data[0])
edges = data[1:]

graph = {}

for edge in edges:
    a, b = map(int, edge.split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
node_list = list(range(1, nodes+1))

visited = set()

component_count = 0

def dfs(start, graph, visited):
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

for node in node_list:
    if node not in visited:
        dfs(node, graph, visited) 
        component_count += 1      

print(component_count - 1)