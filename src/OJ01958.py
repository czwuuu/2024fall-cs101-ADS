three_tower = [0, 1, 3] + [0]*10
for i in range(3, 13):
    three_tower[i] = 2*three_tower[i-1]+1

answer = [0, 1, 3]+[0]*10
for n in range(3, 13):
    ks = [10000000]+[0]*n
    for k in range(1, n+1):
        ks[k] = 2*answer[n-k]+three_tower[k]
    answer[n] = min(ks)
for ans in answer[1:]:
    print(ans)

