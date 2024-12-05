def find_longest_decreasing_seq(arr, k):
    dp = [1]+[0]*(k-1)
    for i in range(1, k):
        li = [dp[j] for j in range(0, i) if arr[j] >= arr[i]] + [0]
        dp[i] = max(li) + 1
    print(max(dp))

k = int(input())
array = list(map(int, input().split()))
find_longest_decreasing_seq(array, k)
