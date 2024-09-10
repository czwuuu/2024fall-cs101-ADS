t = int(input())
ans = ["NO"]*t
for i in range(t):
    abc = list(map(int, input().split()))
    if sum(abc) - 2*max(abc) == 0:
        ans[i] = "YES"
for i in range(t):
    print(ans[i])
