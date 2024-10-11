answer = []
while True:
    p, e, i, d = map(int, input().split())
    if p == -1 and e == -1 and i == -1 and d == -1:
        break
    p = p % 23
    e = e % 28
    i = i % 33
    for date in range(d+1, d+21253):
        if (date-p)%23 == 0 and (date-e)%28 == 0 and (date-i)%33 == 0:
            answer.append(date-d)
for i in range(len(answer)):
    print(f'Case {i+1}: the next triple peak occurs in {answer[i]} days.')