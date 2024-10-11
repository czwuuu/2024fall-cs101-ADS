n = int(input())
max_sum = 0
for a1 in range(0, n+1):
    for a2 in range(0, n+1):
        if (a1+a2)%2 != 0:
            continue
        a3 = 0
        while a3 <= n:
            if (a2+a3)%3 != 0:
                a3 += 1
                continue
            else:
                if (a1+a2+a3)%5==0:
                    max_sum = max(max_sum, a1+a2+a3)
                a3 += 3
print(max_sum)