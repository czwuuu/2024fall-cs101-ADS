from math import ceil

t = int(input())
ans = [0]*t
for i in range(t):
    x, y = map(int, input().split())
    if x <= y:
        ans[i] = y-x
    else:
        n = ceil(x/y)
        ans[i] = n*y - x
for i in range(t):
    print(ans[i])

