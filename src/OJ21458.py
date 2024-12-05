def gain_weight(exercise, T):
    dp = [0] + [-1]*T
    used = [[0]*len(exercise) for _ in range(T+1)]
    for i in range(1, T+1):
        available = [j for j in range(len(exercise)) if i-exercise[j][0]>= 0 and dp[i-exercise[j][0]] > -1]
        if not available:
            dp[i] = -1
        else:
            mark = -1
            for j in available:
                if not used[i-exercise[j][0]][j]:
                    if dp[i-exercise[j][0]]+exercise[j][1] > dp[i]:
                        dp[i] = dp[i-exercise[j][0]]+exercise[j][1]
                        mark = j
            if mark != -1:
                used[i] = used[i-exercise[mark][0]][:]
                used[i][mark] = 1
    return dp[-1]

T, n = map(int, input().split())
exercise = []
for _ in range(n):
    exercise.append(tuple(map(int, input().split())))
print(gain_weight(exercise, T))