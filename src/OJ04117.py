dp = [[0]*51 for _ in range(51)]
for i in range(1, 51):
    dp[0][i] = 1
    dp[i][1] = 1
for i in range(1, 51):
    for j in range(1, 51):
        if j > i:
            dp[i][j] = dp[i][i]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-j][j]

import sys
data = sys.stdin.read()
data = list(map(int, data.splitlines()))
for num in data:
    print(dp[num][-1])