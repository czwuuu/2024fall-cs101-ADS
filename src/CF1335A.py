t = int(input())
ans = [0]*t
for i in range(t):
    n = int(input())
    if n == 1 or n == 2:
        pass
    else:
        ans[i] = (n-1)//2
for i in range(t):
    print(int(ans[i]))
