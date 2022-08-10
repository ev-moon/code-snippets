# only works for uni-directional graphs


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)

    if a < b:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def main():
    v, e = map(int, input().split())
    parent = [i for i in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            print("cycle")
            return
        else:
            union_parent(parent, a, b)


main()