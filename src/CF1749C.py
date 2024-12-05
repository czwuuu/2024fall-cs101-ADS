def check(king, count):
    countcopy = count[:]
    mark = king
    flag = False
    while mark > 0:
        for j in range(mark, 0, -1):
            if countcopy[j] != 0:
                countcopy[j] -= 1
                mark -= 1
                break
        if mark == 0:
            flag = True
            break
        else:
            countcopy[1] -= 1
            if countcopy[1] <= 0:
                flag = False
                break
    return flag



t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counter = [0]*101
    for i in a:
        counter[i] += 1

    k = 0
    while k <=n-1 and check(k+1, counter):
        k += 1
    answer.append(k)
for ans in answer:
    print(ans)