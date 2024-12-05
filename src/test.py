n, m = map(int, input().split())

dsu = [i for i in range(n)]
def find(k):
    return k if dsu[k]==k else find(dsu[k])
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if a != b:
        dsu[b] = a

for _ in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)

print(len(set(dsu)))