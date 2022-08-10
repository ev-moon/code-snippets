from collections import deque

v, e = map(int, input().split())
edges = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
for _ in range(e):
    a, b = map(int, input().split())
    indegree[b] += 1
    edges[a].append(b)


def find_zero_indegree(indegree, visited):
    return [i for i in indegree if indegree[i] == 0 and i not in visited]


queue = []
visited = set()
result = []
queue = deque(find_zero_indegree(indegree, visited))
while queue:
    idx = queue.popleft()
    if idx in visited:
        continue
    visited.add(idx)
    result.append(idx)
    connected_edges = edges[idx]
    for v in connected_edges:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
if len(visited) < v:
    print("cycle")
else:
    print(*result[1:], sep=" ")