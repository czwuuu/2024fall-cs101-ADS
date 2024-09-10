n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
su = 0
ans = 0
s = sum(a)/2
while su <= s:
    su += a[ans]
    ans += 1
print(ans)