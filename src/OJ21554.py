n = int(input())
T = list(map(int, input().split()))
order = [(T[i], i+1) for i in range(n)]
order.sort()
ans = 0
for i in range(n-1):
    ans += (n-1-i)*order[i][0]
ans /= n
print(*[order[i][1] for i in range(n)])
print(f'{ans:.2f}')