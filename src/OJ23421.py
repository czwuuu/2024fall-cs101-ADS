def thief(price: list, weight: list, limit: int, n: int) -> int:
    dp = [0]*(limit+1)
    for i in range(n):
        for j in range(limit, 0, -1):
            if j >= weight[i]:
                new_value = price[i] + dp[j-weight[i]]
                dp[j] = max(dp[j], new_value)
    return dp[-1]

N, B = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))
print(thief(price, weight, B, N))


