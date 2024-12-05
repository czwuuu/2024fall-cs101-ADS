def largest_height_sum(h1, h2, n):
    dp = [[0, 0, 0] for _ in range(n)]

    #initialization
    dp[0][1] = h1[0]
    dp[0][2] = h2[0]

    #evolution
    for i in range(1, n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + h1[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + h2[i]
    return max(dp[-1])

n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
print(largest_height_sum(h1, h2, n))