def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def main():
    v, e = map(int, input().split())
    parent = [i for i in range(v + 1)]
    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    edges.sort()
    total_cost = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
    return total_cost


print(main())