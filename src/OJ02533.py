def find_longest_ordered_subseq(seq, n):
    dp = [1]+[0]*(n-1)
    for i in range(n):
        li = [dp[j] for j in range(0, i) if seq[j] < seq[i]] + [0]
        dp[i] = max(li) + 1
    print(max(dp))

n = int(input())
seq = list(map(int, input().split()))
find_longest_ordered_subseq(seq, n)
