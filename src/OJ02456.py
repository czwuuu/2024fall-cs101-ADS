def binary_search(x, C):
    low, high = 0, (x[-1]-x[0])/(C-1)
    while low <= high:
        mid = (low+high)//2
        if can_reach(mid, x, C):
            low = mid+1
        else:
            high = mid-1
    return int(high)

def can_reach(distance, x, C):
    cnt = 1
    mark = 0
    for i in range(1, len(x)):
        if x[i]-x[mark] >= distance:
            mark = i
            cnt += 1
    return cnt >= C

N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
x.sort()
print(binary_search(x, C))
