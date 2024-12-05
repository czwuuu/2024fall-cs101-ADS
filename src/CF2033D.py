t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    pref_sums = set()
    pref_sum = 0
    for i in range(n):
        pref_sum += a[i]
        if pref_sum in pref_sums or pref_sum == 0:
            cnt += 1
            pref_sum = 0
            pref_sums.clear()
        else:
            pref_sums.add(pref_sum)
    print(cnt)
