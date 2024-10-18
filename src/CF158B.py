from math import ceil

n = int(input())
s = list(map(int, input().split()))

sdict = {1:0,2:0,3:0,4:0}
for si in s:
    sdict[si] += 1

answer = sdict[4] + sdict[3]
sdict[1] = max(0, sdict[1]-sdict[3])
answer += ceil(sdict[2]/2)
sdict[1] = max(0, sdict[1]-2 * (sdict[2]%2))
answer += ceil(sdict[1]/4)

print(int(answer))