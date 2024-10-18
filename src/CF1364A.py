t = int(input())
answer = []
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    sum_mod = 0
    for i in range(n):
        sum_mod += a[i]
        sum_mod %= x

    ans = -1
    found = False
    if sum_mod != 0:
        ans = n
        found = True

    p = 0; q = n-1
    while (not found) and p <= q:
        if a[p]%x != 0 or a[q]%x != 0:
            ans = n-1-p
            found = True
        else:
            p += 1
            q -= 1

    answer.append(ans)

for ans in answer:
    print(ans)

