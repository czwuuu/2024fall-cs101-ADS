from math import ceil
n, m, a = map(int, input().split())
result = ceil(n/a)*ceil(m/a)
print(int(result))
