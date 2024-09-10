t = int(input())
ans = [-1]*t
for i in range(t):
    n = int(input())
    twos = 0
    threes = 0
    while n % 2 == 0:
        twos += 1
        n /= 2
    while n % 3 == 0:
        threes += 1
        n /= 3
    if n == 1 and twos <= threes:
        ans[i] = 2 * threes - twos
for i in range(t):
    print(ans[i])