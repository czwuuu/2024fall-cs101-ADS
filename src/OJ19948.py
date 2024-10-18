n, m = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
d = r[-1]-r[0]

r_diff = [r[i+1]-r[i] for i in range(n-1)]
need_to_d = sum((sorted(r_diff,reverse=True))[:(m-1)])

d -= need_to_d
print(d)
