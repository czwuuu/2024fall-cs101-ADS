t = int(input())
ans = [0]*t
for i in range(t):
    n, k = map(int, input().split())
    forecast = list(map(int, input().split()))
    real = list(map(int, input().split()))
    sorted_forecast = sorted(enumerate(forecast), key = lambda x: x[1])
    ans[i] = [0]*n
    real.sort()
    for j in range(n):
        ans[i][sorted_forecast[j][0]] = real[j]
for i in range(t):
    print(*ans[i])