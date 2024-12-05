def common_subsequence(seq_a: str, seq_b: str) -> int:
    dp = [[0]*(len(seq_a)+1) for _ in range(len(seq_b)+1)]
    longest_subseq_len = 0
    for i in range(1, len(seq_b)+1):
        for j in range(1, len(seq_a)+1):
            if seq_a[j-1] == seq_b[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if dp[i][j] > longest_subseq_len:
                longest_subseq_len = dp[i][j]
    return longest_subseq_len

import sys
datas = sys.stdin.read().splitlines()
for data in datas:
    a, b = data.split()
    print(common_subsequence(a, b))
