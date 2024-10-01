from math import ceil

answers = []
while True:
    N = int(input())
    if N == 0:
        break
    else:
        ans = float('inf')
        for i in range(N):
            v, t = map(int, input().split())
            if t >= 0:
                arrival_t = ceil(t + 4.5*3600/v)
                if arrival_t < ans:
                    ans = arrival_t
        answers.append(ans)
for i in range(len(answers)):
    print(answers[i])