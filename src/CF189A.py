def cut_ribbon(l, a, b, c):
    dp = [0] + [None] * l
    li = [a, b, c]
    for frac in li:
        for i in range(1, l+1):
            if i == frac and dp[i] is None:
                dp[i] = 1
            elif i > frac:
                if not (dp[i - frac] is None):
                    dp[i] = dp[i-frac]+1 if dp[i] is None else max(dp[i], dp[i-frac]+1)
    return dp[-1]

n, a, b, c = map(int, input().split())
print(cut_ribbon(n, a, b, c))