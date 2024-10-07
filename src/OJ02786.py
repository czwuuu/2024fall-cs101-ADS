pell = [0, 1, 2]
for i in range(3, 1000001):
    pell.append((2*pell[i-1]+pell[i-2])%32767)
n = int(input())
answer = []
for i in range(n):
    x = int(input())
    answer.append(pell[x])
for ans in answer:
    print(ans)
