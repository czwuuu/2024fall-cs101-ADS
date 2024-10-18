from math import sqrt
answer = []
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    else:
        locations = [tuple(map(int, input().split())) for _ in range(n)]
        blank_line = input()
        start_end = []
        no_solution = False
        for i in range(n):
            if locations[i][1] > d or locations[i][1] < 0:
                no_solution = True
                break
            start_end.append((locations[i][0] - sqrt(d**2-locations[i][1]**2),locations[i][0] + sqrt(d**2-locations[i][1]**2)))
        if no_solution:
            answer.append(-1)
            continue
        start_end.sort(key=lambda x: (x[1], -x[0]))
        radars = 1
        mark = 0
        for i in range(n):
            if start_end[i][0] > start_end[mark][1]:
                mark = i
                radars += 1
        answer.append(radars)
for i in range(len(answer)):
    print(f'Case {i+1}: {answer[i]}')
