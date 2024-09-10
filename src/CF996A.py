n_str = input()
n_int = int(n_str)
ans = 0
res = n_int
if n_int >= 100:
    res = int(n_str[-2:])
    ans += (n_int - res)/100
if res >= 20:
    ans += res//20
    res -= (res//20)*20
if res >= 10:
    ans += res // 10
    res -= (res // 10) * 10
if res >= 5:
    ans += res // 5
    res -= (res // 5) * 5
ans += res
print(int(ans))