n, M = map(int, input().split())
a = [0]
a.extend(list(map(int, input().split())))
a = a + [M]
t_before = []
s_bef = 0
for i in range(1, n+2, 2):
    s_bef += a[i]-a[i-1]
    t_before.append(s_bef)
t0 = s_bef
tar_num = [a[i] for i in range(1, n+2, 2)]
min_canshu = M
for k in range(len(tar_num)):
    min_canshu = min(min_canshu, tar_num[k]+1+2*(t0-t_before[k]))
answer = t0+M-min_canshu
print(answer)