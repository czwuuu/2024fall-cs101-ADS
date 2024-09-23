n = int(input())
Fx = []
Fy = []
Fz = []
for i in range(n):
    fx, fy, fz = map(int, input().split())
    Fx.append(fx)
    Fy.append(fy)
    Fz.append(fz)

if sum(Fx)==0 and sum(Fy)==0 and sum(Fz)==0:
    print("YES")
else:
    print("NO")