t = int(input())
allowed_a = []
ans = []
for n in range(3,361):
    if 360 % n == 0:
        allowed_a.append(180-360/n)
for i in range(t):
    a = int(input())
    if a in allowed_a:
        ans.append("YES")
    else:
        ans.append("NO")
for i in range(t):
    print(ans[i])