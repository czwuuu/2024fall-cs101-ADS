import bisect
n = int(input())
a = list(map(int, input().split()))
pre_sum = [0]
s = 0
sum_all = sum(a)
pre_eq = []
suf_eq = []
for i in range(n):
    s += a[i]
    if s == sum_all/3 and i < n-1:
        pre_eq.append(i+1)
    if s == 2*sum_all/3 and i < n-1:
        suf_eq.append(i+1)
    pre_sum.append(s)
cnt = 0
length = len(suf_eq)
for j in pre_eq:
    k_ind = bisect.bisect_right(suf_eq, j)
    cnt += length-k_ind
print(cnt)


