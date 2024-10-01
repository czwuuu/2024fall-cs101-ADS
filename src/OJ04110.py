n, wm = map(int, input().split())
v_w = []
total_value = 0
for i in range(n):
    vi, wi = map(int, input().split())
    v_w.append([vi, wi])
v_w.sort(key = lambda x: x[0]/x[1], reverse = True)
count = 0
while wm >= 0:
    wm -= v_w[count][1]
    total_value += v_w[count][0]
    count += 1
    if count >= n:
        break
if wm < 0:
    count -= 1
    total_value -= v_w[count][0]/v_w[count][1]*(-wm)
print(f"{total_value:.1f}")

