from collections import Counter
def boredom(seq):
    m = max(seq)
    ele = set(seq)
    counter = Counter(seq)
    dp = [0]*(m+1)

    #initialzation
    dp[1] = counter.get(1, 0)

    for i in range(2, m+1):
        if i in ele:
            dp[i] = max(dp[i-2]+counter[i]*i, dp[i-1])
        else:
            dp[i] = dp[i-1]
    return dp[m]

n = int(input())
arr = list(map(int, input().split()))
print(boredom(arr))