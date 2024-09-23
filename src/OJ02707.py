from math import sqrt
ans = []
n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    delta = b*b-4*a*c
    if delta > 0:
        x1 = round((-b+sqrt(delta))/(2*a),5)
        x2 = round((-b-sqrt(delta))/(2*a),5)
        ans.append([f"{x1:.5f}", f"{x2:.5f}"])
    elif delta < 0:
        real = round(-b/(2*a),5)
        img = round(sqrt(-delta)/(2*a),5)
        ans.append([f"{real:.5f}+"+f"{img:.5f}i", f"{real:.5f}-"+f"{img:.5f}i"])
    else:
        x = round(-b/(2*a),5)
        ans.append(["equal", f"{x:.5f}"])
for i in range(n):
    if ans[i][0] == "equal":
        print("x1=x2="+ans[i][1])
    else:
        print("x1="+ans[i][0]+";"+"x2="+ans[i][1])