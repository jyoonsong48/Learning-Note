from collections import deque

dataset = """target seq
start seq"""

data = dataset.split("\n")
data = [x for x in data if x != '']
#print(data)

def reverse_segment(arr, i, j):
    new_arr = arr[:]
    new_arr[i:j+1] = arr[i:j+1][::-1]
    return new_arr

def all_reversals(arr):
    results = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            results.append(reverse_segment(arr, i, j))
    return results

def reverse_distance(s1, s2, distance):
    if s1 & s2:
        return distance
    
    new_s1 = set()
    for s in s1:
        for arr in all_reversals(list(s)):
            new_s1.add(tuple(arr))
    new_s2 = set()
    for s in s2:
        for arr in all_reversals(list(s)):
            new_s2.add(tuple(arr))
    
    distance += 2
    
    if s1 & new_s2:
        return distance - 1
    if new_s1 & s2:
        return distance - 1
    if new_s1 & new_s2:
        return distance
    
    return reverse_distance(new_s1, new_s2, distance)

for i in range(1, len(data), 2):
    start = data[i].split()
    target = data[i-1].split()
    print(reverse_distance({tuple(start)}, {tuple(target)}, 0))
