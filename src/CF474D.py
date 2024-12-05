t, k = map(int, input().split())

MOD = 1000000007
MAX = 100000
answer = []

dp = [1]*(MAX+1)
for i in range(2, MAX+1):
    if k == 1:
        dp[1] = 2
    if i-k >= 0:
        dp[i] = (dp[i-1]+dp[i-k])%MOD
    else:
        dp[i] = dp[i-1]

s = 0
pre_sum = [0]
for i in range(1, len(dp)):
    s += dp[i]
    pre_sum.append(s)
for i in range(t):
    a, b = map(int, input().split())
    answer.append((pre_sum[b]-pre_sum[a-1])%MOD)
for ans in answer:
    print(ans)
