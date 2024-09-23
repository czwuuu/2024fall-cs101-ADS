from math import log2

t = int(input())

ans = []

for i in range(t):
    n = int(input())
    max2 = int(log2(n))
    result = n*(n+1)/2
    result -= 2**(max2 + 2)-2
    ans.append(result)
for ans in ans:
    print(int(ans))

