n_nodes = int(input())
n_edges = int(input())

# list 초기화 시 주의
graph = [[float("inf")] * (n_nodes + 1) for _ in range(n_nodes + 1)]

for _ in range(n_edges):
    s, e, dist = map(int, input().split())
    graph[s][e] = dist

for i in range(n_nodes + 1):
    graph[i][i] = 0

for k in range(1, n_nodes + 1):
    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n_nodes + 1):
    for j in range(1, n_nodes + 1):
        print("INFINITY" if graph[i][j] == float("inf") else graph[i][j], end=" ")
    print()
