n = int(input())
len_non_decreasing = 0
a = list(map(int, input().split()))
buffer = 1

for i in range(1, n):
    if a[i] >= a[i-1]:
        buffer += 1
    else:
        if buffer > len_non_decreasing:
            len_non_decreasing = buffer
        buffer = 1

if buffer > len_non_decreasing:
    len_non_decreasing = buffer

print(len_non_decreasing)