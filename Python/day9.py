from sys import maxsize
from itertools import permutations

f = open("../inputs/day9input.txt")
paths = f.readlines()

graph = {}

for path in paths:
    parts = path.strip().split(" ")
    start = parts[0]
    end = parts[2]
    dist = int(parts[-1])
    graph.setdefault(start, {})[end] = dist
    graph.setdefault(end, {})[start] = dist

shortest = maxsize
longest = 0
for perms in permutations(graph):
    dist = sum(map(lambda i, j: graph[i][j], perms[:-1], perms[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print(shortest)
print(longest)
