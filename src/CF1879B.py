t = int(input())
ans = [0]*t
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sa = sum(a)
    sb = sum(b)
    ma = min(a)
    mb = min(b)
    #cost = [[a[i]+b[j] for j in range(n)] for i in range(n)]
    ans[i] = min([sa + n*min(b), sb + n*min(a)])
for i in range(t):
    print(ans[i])
