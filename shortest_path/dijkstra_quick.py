import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
dist = [float("inf")] * (n + 1)
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

heap = [(0, start)]
dist[start] = 0
heapq.heapify(heap)
while heap:
    d, node = heapq.heappop(heap)
    if d > dist[node]:
        continue
    for i in graph[node]:
        cost = dist[node] + i[1]
        if dist[i[0]] > cost:
            dist[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

for i in range(1, n + 1):
    if dist[i] == float("inf"):
        print("INFINTIY")
    else:
        print(dist[i])
