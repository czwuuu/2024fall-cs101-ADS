import bisect
from collections import deque
def minimum_setup_time(seq, n):
    tup = [(seq[2*i], seq[2*i+1]) for i in range(n)]
    tup.sort()
    cnt = 1
    head = deque([tup[0][1]])
    for i in range(1, n):
        ind = bisect.bisect_right(head, tup[i][1])
        if ind == 0:
            cnt += 1
            head.appendleft(tup[i][1])
        else:
            head[ind-1] = tup[i][1]
    return cnt

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minimum_setup_time(arr, n))
