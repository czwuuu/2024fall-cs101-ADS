import bisect
from collections import deque
dp = deque()

N = int(input())
seq = list(map(int, input().split()))
for i in range(N):
    if len(dp) == 0 or dp[0] > seq[i]:
        dp.appendleft(seq[i])
    else:
        ind = bisect.bisect_right(dp, seq[i])
        dp[ind-1] = seq[i]
print(len(dp))