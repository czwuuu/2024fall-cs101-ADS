import bisect
T = int(input())
answer = []
for _ in range(T):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    dp = [p[0]]+[0]*(n-1)
    for i in range(1, n):
        ind = bisect.bisect_left(m, m[i]-k)-1
        if ind >= 0:
            dp[i] = max(dp[i-1], p[i]+dp[ind])
        else:
            dp[i] = max(dp[i-1], p[i])
    answer.append(dp[-1])
for ans in answer:
    print(ans)