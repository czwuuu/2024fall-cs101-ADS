s = input()
m = int(input())
ans = []
A = []
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        A.append(1)
    else:
        A.append(0)

A2 = [0]
s = 0
for i in range(len(A)):
    s += A[i]
    A2.append(s)

for i in range(m):
    li, ri = map(int, input().split())
    ans.append(A2[ri-1]-A2[li-1])
for item in ans:
    print(item)