n, k, l, c, d, p, nl, np = map(int, input().split())
alist = [k*l/(n*nl), c*d/n, p/(n*np)]
alist = list(map(int, alist))
print(min(alist))