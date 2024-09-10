x = list(map(int, input().split()))
m = max(x)
ans = [m-j for j in x if m-j != 0]
print(*ans)

