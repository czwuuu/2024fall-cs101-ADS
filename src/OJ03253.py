answer_list = []
while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    else:
        answer = []
        circle = [i for i in range(n)]
        p = p-1
        while len(circle) > 0:
            p = (p+m-1)%len(circle)
            popper = circle.pop(p)
            answer.append(popper+1)
        answer_list.append(answer)
for answer in answer_list:
    print(','.join(map(str, answer)))
