def change(status, step):
    for i in range(step-1, len(status), step):
        if status[i] == 1:
            status[i] = 0
        else:
            status[i] = 1
    return status

t = int(input())
ans = []
for i in range(t):
    n = int(input())
    status = [0]*n
    for step in range(1, n+1):
        status = change(status, step)
    ans.append(sum(status))

for answer in ans:
    print(answer)
