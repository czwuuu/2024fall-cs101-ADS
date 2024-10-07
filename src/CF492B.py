n, l = map(int, input().split())
a = set(map(int, input().split()))

a = list(a)
a.sort()
ds = [a[0], l-a[-1]]
for i in range(1, len(a)):
    ds.append(0.5*(a[i]-a[i-1]))
d = max(ds)
print(f'{d:.10f}')