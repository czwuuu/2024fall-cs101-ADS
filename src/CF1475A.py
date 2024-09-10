from math import log2
t = int(input())
ans = ["YES"]*t
for i in range(t):
    n = int(input())
    mid = log2(n)
    if isinstance(mid, float) and mid.is_integer():
        ans[i] = "NO"
for i in range(t):
    print(ans[i])
